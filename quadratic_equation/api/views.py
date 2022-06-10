import math

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import EquationSerializer


class Calculator():
    """ Calculator for solving equations. """

    def __init__(self, coefficient1, coefficient2, coefficient3):
        self.coefficient1 = coefficient1
        self.coefficient2 = coefficient2
        self.coefficient3 = coefficient3

    def get_answer(self):
        """ Calculate equation. """

        if not any([self.coefficient1, self.coefficient2, self.coefficient3]):
            return 'Roots can be any numbers', ()
        if self.coefficient1:
            roots = self.__calculate_quadratic_equation()
            if len(roots) == 2:
                return 'Two roots', roots
            if len(roots) == 1:
                return 'One root', roots
            return 'Not roots', ()

        root = self.__calculate_linear_equation()
        if root:
            return 'One root', root
        return 'Not roots', ()

    def __calculate_linear_equation(self):
        """ Solution of linear equation. """

        if self.coefficient2:
            return (round(-self.coefficient3 / self.coefficient2, 2),)
        return ()

    def __calculate_quadratic_equation(self):
        """ Solution of quadratic equation. """

        discriminant = self.__get_discriminant()
        if discriminant < 0:
            return ()
        if discriminant == 0:
            return (round(-self.coefficient2 / (2*self.coefficient1), 2),)
        root1 = round(
            (-self.coefficient2+math.sqrt(discriminant))
            /(2*self.coefficient1),
            2,
        )
        root2 = round(
            (-self.coefficient2-math.sqrt(discriminant))/
            (2*self.coefficient1),
            2
        )
        return (root1, root2)

    def __get_discriminant(self):
        """ Calculate discriminant of quadratic equation. """

        return self.coefficient2**2 - 4*self.coefficient1*self.coefficient3


class AnswerViewSet(viewsets.ViewSet):
    def create(self, request):
        coefficient_1 = request.query_params.get('a', 0)
        coefficient_2 = request.query_params.get('b', 0)
        coefficient_3 = request.query_params.get('c', 0)
        answer = Calculator(
            float(coefficient_1),
            float(coefficient_2),
            float(coefficient_3),
        ).get_answer()
        serializer = EquationSerializer(
            data={
                'coefficient_1': coefficient_1,
                'coefficient_2': coefficient_2,
                'coefficient_3': coefficient_3,
                'root_1': None if len(answer[1]) < 1 else answer[1][0],
                'root_2': None if len(answer[1]) < 2 else answer[1][1],
                'answer': answer[0],
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
