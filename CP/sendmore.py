from google.apputils import app
import gflags
from ortools.constraint_solver import pywrapcp

FLAGS = gflags.FLAGS


def main(unused_argv):
  # Create the solver.
  solver = pywrapcp.Solver('SEND + MORE = MONEY')

  digits = range(0, 10)
  s = solver.IntVar(digits, 's')
  e = solver.IntVar(digits, 'e')
  n = solver.IntVar(digits, 'n')
  d = solver.IntVar(digits, 'd')
  m = solver.IntVar(digits, 'm')
  o = solver.IntVar(digits, 'o')
  r = solver.IntVar(digits, 'r')
  y = solver.IntVar(digits, 'y')

  letters = [s, e, n, d, m, o, r, y]

  solver.Add(1000 * s + 100 * e + 10 * n + d + 1000 * m + 100 * o + 10 * r + e ==
             10000 * m + 1000 * o + 100 * n + 10 * e + y)

  # pylint: disable=g-explicit-bool-comparison
  solver.Add(s != 0)
  solver.Add(m != 0)

  solver.Add(solver.AllDifferent(letters))

  solver.NewSearch(solver.Phase(letters,
                                solver.INT_VAR_DEFAULT,
                                solver.INT_VALUE_DEFAULT))
  solver.NextSolution()
  print letters
  solver.EndSearch()


if __name__ == '__main__':
  app.run()
