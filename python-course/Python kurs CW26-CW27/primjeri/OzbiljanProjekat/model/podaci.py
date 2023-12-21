from model.core import Parameter, Variable, Function, Module


def getPodaci():
    m = Module("main", True)

    f = Function("suma", "float", "math.h")
    f.add_element(Parameter("x1", "float", True))
    f.add_element(Parameter("x2", "float", True))

    m.add_element(f)

    f = Function("razlika", "float", "math.h")
    f.add_element(Parameter("x1", "float", True))
    f.add_element(Parameter("x2", "float", True))

    m.add_element(f)

    f = Function("proizvod", "float", "math.h")
    f.add_element(Parameter("x1", "float", False))
    f.add_element(Parameter("x2", "float", True))

    m.add_element(f)

    m.add_element(Variable("var1", "float", value="3"))
    m.add_element(Variable("var2", "int"))
    m.add_element(Variable("var3", "int", value="36"))

    m.add_element(Variable("res1", "float"))
    m.add_element(Variable("res2", "float"))
    m.add_element(Variable("res3", "float"))

    m.add_call("suma", "res1", "var1", "15")
    m.add_call("razlika", "res2", "24", "var2")
    m.add_call("proizvod", "res3", "var3", "17")
    d = {}
    d[m.name] = m
    o = getOstaliPodaci()
    d[o.name] = o
    return d


def getOstaliPodaci():
    m = Module("ostalo")

    f = Function("suma3", "float", "math.h")
    f.add_element(Parameter("x1", "float", True))
    f.add_element(Parameter("x2", "float", True))

    m.add_element(f)

    f = Function("razlika3", "float", "math.h")
    f.add_element(Parameter("x1", "float", True))
    f.add_element(Parameter("x2", "float", True))

    m.add_element(f)

    f = Function("proizvod3", "float", "math.h")
    f.add_element(Parameter("x1", "float", True))
    f.add_element(Parameter("x2", "float", True))

    m.add_element(f)

    return m
