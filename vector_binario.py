# -*- coding: utf-8 -*-
# !/usr/bin/python


def vector_binario(decimal, nelementos):

    binario = []

    while decimal // 2 != 0:
        binario = [decimal % 2] + binario
        decimal = decimal // 2
    binario = [decimal] + binario
    binario = [0] * (nelementos - len(binario)) + binario
    return binario