# Hard coded moves to perform on the cube.
# location is passed in and returned with the stickers in the order they should be after the turn.

# Front Quarter Turn Clockwise
def F(loc):
	return (loc[6] + loc[14] + loc[2] +
			loc[3] + loc[5] + loc[13] +
			loc[19] + loc[7] + loc[8] +
			loc[9] + loc[10] + loc[1] +
			loc[4] + loc[12] + loc[18] +
			loc[15] + loc[16] + loc[0] +
			loc[11] + loc[17] + loc[20])

# Front Quarter Turn Counterclockwise
def Fp(loc):
	return (loc[17] + loc[11] + loc[2] +
			loc[3] + loc[12] + loc[4] +
			loc[0] + loc[7] + loc[8] +
			loc[9] + loc[10] + loc[18] +
			loc[13] + loc[5] + loc[1] +
			loc[15] + loc[16] + loc[19] +
			loc[14] + loc[6] + loc[20])

# Front Half Turn
def F2(loc):
	return (loc[19] + loc[18] + loc[2] +
			loc[3] + loc[13] + loc[12] +
			loc[17] + loc[7] + loc[8] +
			loc[9] + loc[10] + loc[14] +
			loc[5] + loc[4] + loc[11] +
			loc[15] + loc[16] + loc[6] +
			loc[1] + loc[0] + loc[20])

# Right Quarter Turn Clockwise
def R(loc):
	return (loc[12] + loc[1] + loc[2] +
			loc[4] + loc[18] + loc[5] +
			loc[6] + loc[7] + loc[8] +
			loc[0] + loc[11] + loc[17] +
			loc[20] + loc[13] + loc[14] +
			loc[3] + loc[10] + loc[16] +
			loc[15] + loc[19] + loc[9])

# Right Quarter Turn Counterclockwise
def Rp(loc):
	return (loc[9] + loc[1] + loc[2] +
			loc[15] + loc[3] + loc[5] +
			loc[6] + loc[7] + loc[8] +
			loc[20] + loc[16] + loc[10] +
			loc[0] + loc[13] + loc[14] +
			loc[18] + loc[17] + loc[11] +
			loc[4] + loc[19] + loc[12])

# Right Half Turn
def R2(loc):
	return (loc[20] + loc[1] + loc[2] +
			loc[18] + loc[15] + loc[5] +
			loc[6] + loc[7] + loc[8] +
			loc[12] + loc[17] + loc[16] +
			loc[9] + loc[13] + loc[14] +
			loc[4] + loc[11] + loc[10] +
			loc[3] + loc[19] + loc[0])

# Up Quarter Turn Clockwise
def U(loc):
	return (loc[3] + loc[0] + loc[1] +
			loc[2] + loc[10] + loc[11] +
			loc[4] + loc[5] + loc[6] +
			loc[7] + loc[8] + loc[9] +
			loc[12] + loc[13] + loc[14] +
			loc[15] + loc[16] + loc[17] +
			loc[18] + loc[19] + loc[20])

# Up Quarter Turn Counterclockwise
def Up(loc):
	return (loc[1] + loc[2] + loc[3] +
			loc[0] + loc[6] + loc[7] +
			loc[8] + loc[9] + loc[10] +
			loc[11] + loc[4] + loc[5] +
			loc[12] + loc[13] + loc[14] +
			loc[15] + loc[16] + loc[17] +
			loc[18] + loc[19] + loc[20])

# Up Half Turn
def U2(loc):
	return (loc[2] + loc[3] + loc[0] +
			loc[1] + loc[8] + loc[9] +
			loc[10] + loc[11] + loc[4] +
			loc[5] + loc[6] + loc[7] +
			loc[12] + loc[13] + loc[14] +
			loc[15] + loc[16] + loc[17] +
			loc[18] + loc[19] + loc[20])