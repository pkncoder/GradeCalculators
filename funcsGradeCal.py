def NumToGPAFunc(grd):
    if grd >= 90:
        return 'A'
    elif grd >= 80:
        return 'B'
    elif grd >= 70:
        return 'C'
    elif grd >= 60:
        return 'D'
    elif grd >= 0:
        return 'F'
    else:
        return 'done'