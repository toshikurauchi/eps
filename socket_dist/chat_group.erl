%% ---
%%  Excerpted from "Programming Erlang",
%%  published by The Pragmatic Bookshelf.
%%  Copyrights apply to this code. It may not be used to create training material, 
%%  courses, books, articles, and the like. Contact us if you are in doubt.
%%  We make no guarantees that this code is fit for any purpose. 
%%  Visit http://www.pragmaticprogrammer.com/titles/jaerlang for more book information.
%%---

-module(chat_group).
-import(lib_chan_mm, [send/2, controller/2]).
-import(lists, [foreach/2, reverse/2]).

-export([start/2]).

start(C, Nick) ->
    process_flag(trap_exit, true),
    controller(C, self()),
    send(C, ack),
    self() ! {chan, C, {relay, Nick, "I'm starting the group"}},
    group_controller([{C,Nick}]).



delete(Pid, [{Pid,Nick}|T], L) -> {Nick, reverse(T, L)};
delete(Pid, [H|T], L)          -> delete(Pid, T, [H|L]);
delete(_, [], L)               -> {"????", L}.



group_controller([]) ->
    exit(allGone);
group_controller(L) ->
    receive
	{chan, C, {relay, Nick, Str}} ->
	    foreach(fun({Pid,_}) -> send(Pid, {msg,Nick,C,Str}) end, L),
	    group_controller(L);
	% Sends a personal message
	{chan, C, {personal, Nick, Str, To}} ->
	    foreach(fun(Receiver) -> send(find_by_nick(L,Receiver), {msg,Nick,C,Str}) end, To),
	    group_controller(L);
	{login, C, Nick, Groups} ->
	    controller(C, self()),
	    send(C, ack),
	    NewL = [{C,Nick}|L],
	    Nicks = nicksList(NewL,[]),
	    foreach(fun({Pid,_}) -> send(Pid, {resetList,C,Nicks}) end, NewL),
	    % Sets groups list for this user
	    send(C, {refreshGroups,Groups}),
	    self() ! {chan, C, {relay, Nick, "I'm joining the group"}},
	    group_controller(NewL);
	% Refreshes groups list for all users
	{refreshGroups, Groups} ->
	    foreach(fun({Pid,_}) -> send(Pid, {refreshGroups,Groups}) end, L),
	    group_controller(L);
	{chan_closed, C} ->
	    {Nick, L1} = delete(C, L, []),
	    Nicks = nicksList(L1,[]),
	    foreach(fun({Pid,_}) -> send(Pid, {resetList,C,Nicks}) end, L1),
	    self() ! {chan, C, {relay, Nick, "I'm leaving the group"}},
	    group_controller(L1);
	Any ->
	    io:format("group controller received Msg=~p~n", [Any]),
	    group_controller(L)
    end.

nicksList([], Nicks)              -> Nicks;
nicksList([{_Pid,Nick}|T], Nicks) -> nicksList(T, [Nick|Nicks]).

% Returns Pid of the Receiver
find_by_nick([],Receiver) ->
    self();
find_by_nick([{Pid,Receiver}|_T],Receiver) ->
    Pid;
find_by_nick([{_Pid,_Nick}|T],Receiver) ->
    find_by_nick(T,Receiver).
