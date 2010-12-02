package pfc

private case class Term(coef: Double, exp: Int) {
  require(coef != 0 && exp >= 0)
  def compareExp(that: Term) = this.exp - that.exp
}

class Pol private (private val terms: List[Term]) {

  // construtor auxiliar
  // (n.b.: tanto o construtor primario como o auxiliar sao privados)
  private def this(coef: Double, exp: Int) = this(List(Term(coef, exp)))

  // aritmetica de polinomios
  def + (that: Pol): Pol = Pol(Pol.add(this.terms, that.terms))
  def - (that: Pol): Pol = Pol(Pol.add(this.terms, (-that).terms))
  def * (that: Pol): Pol = this
  def / (that: Pol): Tuple2[Pol, Pol] = new Tuple2(this, this)

  // operadores unarios
  def unary_+ : Pol = this
  def unary_- : Pol = {
	  var negTerms:List[Term] = List()
	  for(term <- this.terms) {
	 	  negTerms = negTerms++List(Term(-term.coef, term.exp))
	  }
	  Pol(negTerms)
  }

  // aritmetica mista (o operando 1 e' um polinomio, o operando 2 e' um numero)
  def + (d: Double): Pol = this
  def - (d: Double): Pol = this
  def * (d: Double): Pol = this
  def / (d: Double): Pol = this

  // grau, potenciacao e derivacao
  def degree: Int = 0
  def ^(n: Int): Pol = this
  def deriv: Pol = this
  def ! : Pol = this

  // calcula o valor do polinomio alvo para um dado valor de x
  def apply(x: Double): Double = 0

  // composicao do polinomio alvo com outro polinomio
  def apply(that: Pol): Pol = this

  // sobrescrita de metodos da classe Any
  override def equals(other: Any): Boolean = true
  override def hashCode: Int = 0
  override def toString = {
	  var string = ""
	  
	  for(term <- this.terms) {
	 	  string += formatedString(term)
  	  }
  	  string
  }
  private def formatedString(term: Term) = {
	var string = ""
	if(term.coef != 1 || term.exp == 0) {
	  if(term.coef == -1 && term.exp != 0)
		string += "-"
	  else
		string += term.coef
	}
	if(term.exp != 0) {
	  string += "x"
	  if(term.exp != 1) string += "^" + term.exp
	}
	string
  }

  // metodo auxiliar que multiplica o polinomio alvo por um termo simples
  private def * (term: Term): Pol = new Pol(Nil)
}

object Pol {

  // conversao implicita de Double em Pol
  implicit def doubleToPol(d: Double): Pol = Pol(d)

  // metodos de fabrica acessiveis para os clientes
  def apply(coef: Double, exp: Int): Pol = new Pol(coef, exp)
  def apply(coef: Double): Pol = new Pol(coef, 0)

  // metodo de fabrica interno (serve apenas para evitar o uso de new)
  private def apply(terms: List[Term]): Pol = new Pol(terms)

  // metodo auxiliar para as operacoes de adicao e subtracao de polinomios
  private def add(terms1: List[Term], terms2: List[Term]): List[Term] = add(terms1, terms2, List())
  
  private def add(terms1: List[Term], terms2: List[Term], Acc: List[Term]): List[Term] = {
	  terms1 match {
	 	  case List() => Acc++terms2
	 	  case _ => terms2 match {
	 	 	  case List() => Acc++terms1
	 	 	  case _ => if(terms1.head.compareExp(terms2.head) == 0) add(terms1.tail, terms2.tail, Acc++List(Term(terms1.head.coef + terms2.head.coef, terms1.head.exp)))
	 	 	  			else if(terms1.head.compareExp(terms2.head) < 0) add(terms1, terms2.tail, Acc++List(terms2.head))
	 	 	  			else add(terms1.tail, terms2, Acc++List(terms1.head))
	 	  }
	  }
  }
}