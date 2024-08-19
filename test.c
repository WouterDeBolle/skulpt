int dead = 0;
int alive = 1;

int getCellStatus(int status, int neighboursCount) {
	switch(neighboursCount) {
		case 3:
			status = alive;
			break;
		case 2:
			break;
		default:
			status = dead;
	}

	return status;
}
