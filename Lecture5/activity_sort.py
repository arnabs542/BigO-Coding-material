class Activity:
	def __init__(self, start, finish):
		self.start = start
		self.finish = finish


def activity_selection(a):
	a.sort(key=lambda activity: activity.finish)
	i = 0
	res.append(a[0])
	for j in range(1, len(a)):
		if a[j].start >= a[i].finish:
			res.append(a[j])
			i = j


def print_activities(result):
	for activity in result:
		print('{} - {}'.format(activity.start, activity.finish))


if __name__ == '__main__':
	a = []
	res = []
	n = int(input())
	for i in range(n):
		s, f = map(int, input().split())
		a.append(Activity(s, f))
	
	activity_selection(a)
	print_activities(res)
