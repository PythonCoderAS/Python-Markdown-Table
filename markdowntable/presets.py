from markdowntable import Table as table

def twoxtwo(col1, col2, row1, row2):
	twoxtwotable = table(str(col1))
	twoxtwotable.add_column(str(col2))
	twoxtwotable.finalize_cols()
	twoxtwotable.add_row([str(row1), str(row2)])
	return twoxtwotable.get_table()
	
	
def threexthree(col1,col2,col3,row1_1,row1_2,row1_3, row2_1,row2_2, row2_3):
	threexthreetable = table(str(col1))
	threexthreetable.add_column(str(col2))
	threexthreetable.add_column(str(col3))
	threexthreetable.finalize_cols()
	threexthreetable.add_row([str(row1_1),str(row1_2),str(row1_3)])
	threexthreetable.add_row([str(row2_1),str(row2_2),str(row2_3)])
	return threexthreetable.get_table()

	
def 4x4(col1,col2,col3,col4,row1_1,row1_2,row1_3,row1_4,row2_1,row2_2, row2_3,row2_4,row3_1,row3_2,row3_3,row3_4):
	4x4table = table(str(col1))
	fourxfourtable.add_column(str(col2))
	fourxfourtable.add_column(str(col3))
	fourxfourtable.add_column(str(col4))
	fourxfourtable.finalize_cols()
	fourxfourtable.add_row([str(row1_1),str(row1_2),str(row1_3),str(row1_4)])
	fourxfourtable.add_row([str(row2_1),str(row2_2),str(row2_3),str(row2_4)])
	fourxfourtable.add_row([str(row3_1),str(row3_2),str(row3_3),str(row3_4)])
	return fourxfourtable.get_table()