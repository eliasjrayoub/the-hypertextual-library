import sys


book_num = 0
lines = list(sys.stdin)
to_print = []
for i in range(len(lines)):
	# if (i > 10 and i < len(lines) - 10 and lines[i] != "\n" and "chapter" in lines[i].lower() and lines[i - 1] == "\n" and 
	# 	lines[i - 2] == "\n" and lines[i - 3] == "\n" and lines[i + 1] == "\n"):
	if (i > 10 and "--------" in lines[i]):
			to_print.pop()
			to_print.pop()
			to_print.pop()
			to_print.pop()
			to_print.append(lines[i])
			# line = lines[i].strip()
			# line = line[0] + line[1:7].lower() + line[7:]
			# line = line.replace(".","")
			# to_print.append("-------- %s --------\n" % line)
			# sys.stderr.write(line + "\n")
	else:
		to_print.append(lines[i])

print ''.join(to_print)