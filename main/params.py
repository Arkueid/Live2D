class StandardParams:
    PARAM_ANGLE_X = "PARAM_ANGLE_X"
    PARAM_ANGLE_Y = "PARAM_ANGLE_Y"
    PARAM_ANGLE_Z = "PARAM_ANGLE_Z"
    PARAM_EYE_L_OPEN = "PARAM_EYE_L_OPEN"
    PARAM_EYE_R_OPEN = "PARAM_EYE_R_OPEN"
    PARAM_EYE_L_SMILE = "PARAM_EYE_L_SMILE"
    PARAM_EYE_R_SMILE = "PARAM_EYE_R_SMILE"
    PARAM_EYE_BALL_X = "PARAM_EYE_BALL_X"
    PARAM_EYE_BALL_Y = "PARAM_EYE_BALL_Y"
    PARAM_EYE_BALL_FORM = "PARAM_EYE_BALL_FORM"
    PARAM_BROW_L_X = "PARAM_BROW_L_X"
    PARAM_BROW_L_Y = "PARAM_BROW_L_Y"
    PARAM_BROW_L_ANGLE = "PARAM_BROW_L_ANGLE"
    PARAM_BROW_L_FORM = "PARAM_BROW_L_FORM"
    PARAM_BROW_R_X = "PARAM_BROW_R_X"
    PARAM_BROW_R_Y = "PARAM_BROW_R_Y"
    PARAM_BROW_R_ANGLE = "PARAM_BROW_R_ANGLE"
    PARAM_BROW_R_FORM = "PARAM_BROW_R_FORM"
    PARAM_MOUTH_OPEN_Y = "PARAM_MOUTH_OPEN_Y"
    PARAM_MOUTH_FORM = "PARAM_MOUTH_FORM"
    PARAM_SMILE = "PARAM_SMILE"
    PARAM_TERE = "PARAM_TERE"
    PARAM_BODY_ANGLE_X = "PARAM_BODY_ANGLE_X"
    PARAM_BODY_ANGLE_Z = "PARAM_BODY_ANGLE_Z"
    PARAM_BREATH = "PARAM_BREATH"
    PARAM_HAIR_FRONT = "PARAM_HAIR_FRONT"
    PARAM_HAIR_SIDE = "PARAM_HAIR_SIDE"
    PARAM_HAIR_BACK = "PARAM_HAIR_BACK"
    PARAM_HAIR_FUWA = "PARAM_HAIR_FUWA"
    PARAM_SHOULDER_X = "PARAM_SHOULDER_X"
    PARAM_BUST_X = "PARAM_BUST_X"
    PARAM_BUST_Y = "PARAM_BUST_Y"
    PARAM_BASE_X = "PARAM_BASE_X"
    PARAM_BASE_Y = "PARAM_BASE_Y"


class Parameter:

    def __init__(self):
        self.id: str = ""
        # [DEPRECATED] never used in models versioned cubism 2.1
        self.type: int = 0
        self.value: float = 0
        self.max: float = 0
        self.min: float = 0
        self.default: float = 0

    def __str__(self):
        return f"Parameter(id={self.id}, type={self.type}, value={self.value}, max={self.max}, min={self.min}, default={self.default})"
