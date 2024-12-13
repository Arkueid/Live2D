﻿from core.deformer import RotationDeformer, AffineEnt, WarpDeformer
from core.draw import Mesh
from core.model import ModelImpl, Avatar, PartsData
from core.param import PivotManager, ParamPivots, ParamDefF, ParamDefSet


class Live2DObjectFactory:

    @staticmethod
    def create(clsNo):
        if clsNo < 100:
            if clsNo == 65:
                return WarpDeformer()
            elif clsNo == 66:
                return PivotManager()
            elif clsNo == 67:
                return ParamPivots()
            elif clsNo == 68:
                return RotationDeformer()
            elif clsNo == 69:
                return AffineEnt()
            elif clsNo == 70:
                return Mesh()
        elif clsNo < 150:
            if clsNo == 131:
                return ParamDefF()
            elif clsNo == 133:
                return PartsData()
            elif clsNo == 136:
                return ModelImpl()
            elif clsNo == 137:
                return ParamDefSet()
            elif clsNo == 142:
                return Avatar()

        raise RuntimeError("Unknown class ID: " + str(clsNo))