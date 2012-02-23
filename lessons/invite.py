#!/usr/local/bin/python3
invites = {}
options = ['add', 'list', 'approve', 'delete', 'quit']
prompt = 'Pick an option from the list (%s): ' % ', '.join(options)
status_1 = 'unapproved'
status_2 = 'approved'
while True:
	inp = input(prompt)
	if inp not in options:
		print('Plese pick a valid option')
		continue
	if inp == 'add':
		name = input('Enter name: ')
		if not name:
			continue
		invites[name] = status_1
	elif inp == 'list':
		for name, status in invites.items():
			print('%s (%s)' % (name, status))
	elif inp == 'approve':
		for name in invites:
			if invites[name] == status_1:
				break
		else:
			print('There must be %s status invites. Please pick another option' % status_1)
			continue
		while True:
			print('Please enter a valid name from the list below')
			unapproved = []
			for name in invites:
				if invites[name] == status_1:
					unapproved.append(name)
			print(", ".join(unapproved))
			name = input('Enter name: ')
			if not name:
				break # user changed mind about approving
			if name in unapproved:
				invites[name] = status_2
				print('%s %s' % (name, status_2))
				break
	elif inp == 'delete':
		if not invites:
			print('There must be invites before you delete any of them')
			continue # user changed mind about deleting
		while True:
			print('Please enter a valid name from the list below')
			for name, status in invites.items():
				print('%s (%s)' % (name, status))
			name = input('Enter name: ')	
			if not name:
				break
			if name in invites:
				del invites[name]
				print('%s deleted' % name)
				break
	elif inp == 'quit':
		print('Quitting invites')
		print('The final invitation list follows')
		for name, status in invites.items():
			print('%s (%s)' % (name, status))
		break