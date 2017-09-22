from sys import argv
from os import getcwd, chdir
from subprocess import call

commands = ['help', 'make', 'delete', 'remove', 'rm', 'list', 'ls']
resdir = getcwd()
ProjectDir = '/Users/stevenlandis/Documents/Programming/project/'

if len(argv) < 2:
	#the user didn't give a command, show the help document
	print(open(ProjectDir + 'help.txt', 'r').read())
elif argv[1] == "help":
	print(open(ProjectDir + 'help.txt', 'r').read())
elif argv[1] == 'make':
	#make command: make a new project
	if len(argv) < 3:
		#the user has to specify a project name
		print("Usage: project make [project name]")
	elif argv[2] in commands:
		print("Project name cannot be a command")
	else:
		newName = argv[2]

		#open the data file to see if project name already exists
		f = open(ProjectDir + 'data.txt', 'r')
		txt = f.read().split('\n')
		f.close()
		found = False
		for line in txt:
			if line.split(' ')[0] == newName:
				print("Error: project name already exists")
				found = True
				break

		if not found:
			if txt[0] == '':
				#data file is empty, add to first line
				txt[0] = newName + ' ' + getcwd()
			else:
				#data file has data, append to end
				txt.append(newName + ' '+getcwd())

			#save changes to data file
			f = open(ProjectDir + 'data.txt', 'w')
			f.write('\n'.join(txt))
			f.close()

elif argv[1] in ['delete', 'remove', 'rm']:
	if len(argv) < 3:
		print("Usage: project delete [project name]")
	else:
		name = argv[2]
		#open data file to search for project to delete
		f = open(ProjectDir + 'data.txt', 'r')
		txt = f.read().split('\n')
		f.close()
		found = False
		for i in range(len(txt)):
			if txt[i].split(' ')[0] == name:
				print("Deleting project "+name)
				del txt[i]
				found = True
				break
		if found:
			#save changes to data file
			f = open(ProjectDir + 'data.txt', 'w')
			f.write('\n'.join(txt))
			f.close()
		else:
			print("Project named "+name+" does not exist")

elif argv[1] in ['list', 'ls']:
	#open the data file to get list of projects
	f = open(ProjectDir + 'data.txt', 'r')
	txt = f.read().split('\n')
	f.close()

	if txt[0] == '':
		print("No existing projects")
	else:
		#print the projects
		for line in txt:
			info = line.split(' ')
			print(info[0]+"\n  "+info[1])
else:
	#switch to the specified project name
	name = argv[1]

	#search the data file for the specified project
	f = open(ProjectDir + 'data.txt', 'r')
	txt = f.read().split('\n')
	f.close()
	found = False
	for line in txt:
		if line.split(' ')[0] == name:
			found = True
			print('Project found, opening')
			resdir = ' '.join(line.split(' ')[1:])

			#open the project directory using Sublime Text
			call(['open', '-a', 'Sublime Text', resdir])
			break
	if not found:
		print("Unable to find project named "+name)
	
f = open(ProjectDir + 'dir.txt', 'w')
f.write(resdir)
f.close()