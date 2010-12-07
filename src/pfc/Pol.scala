package pfc

private case class Term(coef: Double, exp: Int) {
  require(coef != 0 && exp >= 0)
  def compareExp(that: Term) = this.exp - that.exp

  override def toString = {
    var string = ""
    if ((this.coef != 1 && this.coef != -1) || this.exp == 0) {
      if(this.coef.toInt == this.coef) string += this.coef.toInt.abs
      else string += this.coef.abs
    }
    if (this.exp != 0) {
      string += "x"
      if (this.exp != 1) string += "^" + this.exp
    }
    string
  }

  def /(that: Term): Term = if (this.exp < that.exp) null
  							else Term(this.coef / that.coef, this.exp - that.exp)
}

class Pol private (private val terms: List[Term]) {

  // construtor auxiliar
  // (n.b.: tanto o construtor primario como o auxiliar sao privados)
  private def this(coef: Double, exp: Int) = this(List(Term(coef, exp)))

  // aritmetica de polinomios
  def +(that: Pol): Pol = Pol(Pol.add(this.terms, that.terms))
  def -(that: Pol): Pol = Pol(Pol.add(this.terms, (-that).terms))
  def *(that: Pol): Pol = that.terms.foldLeft(Pol(Nil))((acc: Pol, term: Term) ⇒ acc + (this * term))
  def /(that: Pol): Tuple2[Pol, Pol] = divideR(this, that, Pol(Nil))

  // metodo auxiliar recursivo para a divisao
  def divideR(dividend: Pol, divisor: Pol, quotient: Pol): Tuple2[Pol, Pol] = {
    require(!divisor.terms.isEmpty)
    if (dividend.terms.isEmpty || dividend.degree < divisor.degree) {
      (quotient, dividend)
    } else {
      var partial = dividend.terms.head / divisor.terms.head
      divideR(dividend - (divisor * partial), divisor, quotient + Pol(List(partial)))
    }
  }

  // operadores unarios
  def unary_+ : Pol = this
  def unary_- : Pol = {
    var negTerms: List[Term] = List()
    for (term ← this.terms) {
      negTerms = negTerms ++ List(Term(-term.coef, term.exp))
    }
    Pol(negTerms)
  }

  // aritmetica mista (o operando 1 e' um polinomio, o operando 2 e' um numero)
  def +(d: Double): Pol = this + Pol(d)
  def -(d: Double): Pol = this - Pol(d)
  def *(d: Double): Pol = this * Pol(d)
  def /(d: Double): Pol = (this / Pol(d))_1

  // grau, potenciacao e derivacao
  def degree: Int = if (this.terms.isEmpty) 0
  else this.terms.head.exp
  def ^(n: Int): Pol = if(n == 0) Pol(1)
  					   else this*(this^n-1)
  def deriv: Pol = Pol(this.terms.filter(term => term.exp > 0).map(term => Term(term.coef * term.exp, term.exp - 1)))
  def ! : Pol = this.deriv

  // calcula o valor do polinomio alvo para um dado valor de x
//  def apply(x: Double): Double = this.terms.foldLeft(0)((acc:Double, term:Term) => acc + (term.coef * )

  // composicao do polinomio alvo com outro polinomio
  def apply(that: Pol): Pol = this.terms.foldLeft(Pol(Nil))((acc: Pol, term: Term) => acc + (Pol(term.coef) * (that^(term.exp))))

  // sobrescrita de metodos da classe Any
  override def equals(other: Any): Boolean = other match {
    case that: Pol ⇒ (this.terms -- that.terms).isEmpty
    case _ ⇒ false
  }
  override def hashCode: Int = 0
  override def toString = {
    var string = ""

    if (!terms.isEmpty) {
      if (terms.head.coef < 0) string += "-"
      string += terms.head
      for (term ← this.terms.tail) {
    	  if (term.coef < 0) string += " - "
    		  else string += " + "
    			  string += term
      }
    }
    else string = "0"
    string
  }

  // metodo auxiliar que multiplica o polinomio alvo por um termo simples
  private def *(term: Term): Pol = Pol(this.terms.map(t ⇒ Term(t.coef * term.coef, t.exp + term.exp)))
}

object Pol {

  // conversao implicita de Double em Pol
  implicit def doubleToPol(d: Double): Pol = Pol(d)

  // metodos de fabrica acessiveis para os clientes
  def apply(coef: Double, exp: Int): Pol = if(coef != 0) new Pol(coef, exp)
  										   else new Pol(Nil)
  def apply(coef: Double): Pol = Pol(coef, 0)

  // metodo de fabrica interno (serve apenas para evitar o uso de new)
  private def apply(terms: List[Term]): Pol = new Pol(terms)

  // metodo auxiliar para as operacoes de adicao e subtracao de polinomios
  private def add(terms1: List[Term], terms2: List[Term]): List[Term] = add(terms1, terms2, List())

  private def add(terms1: List[Term], terms2: List[Term], Acc: List[Term]): List[Term] = {
    terms1 match {
      case List() ⇒ Acc ++ terms2
      case _ ⇒
        terms2 match {
          case List() ⇒ Acc ++ terms1
          case _ ⇒
            if (terms1.head.compareExp(terms2.head) == 0) {
              var newAcc = if (terms1.head.coef + terms2.head.coef != 0) Acc ++ List(Term(terms1.head.coef + terms2.head.coef, terms1.head.exp))
              else Acc
              add(terms1.tail, terms2.tail, newAcc)
            } else if (terms1.head.compareExp(terms2.head) < 0) add(terms1, terms2.tail, Acc ++ List(terms2.head))
            else add(terms1.tail, terms2, Acc ++ List(terms1.head))
        }
    }
  }
}