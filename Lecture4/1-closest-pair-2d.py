import math

INF = 1e9
class Point:
    def __init__(self, x=0,y=0):
      self.x = x
      self.y = y


def distance(p1, p2):
    x = p1.x - p2.x
    y = p1.y - p2.y
    return math.sqrt(x*x + y*y)


def bruteForce(points, left , right):
    min_dist = INF
    for i in range(left, right):
        for j in range(i+1, right):
            min_dist = min(min_dist, distance(points[i], points[j]))

    return min_dist



def minimalDistance(xPoints, yPoints, left, right):
    if right - left <= 3:
        return bruteForce(xPoints, left, right)

    mid = (right + left) // 2
    #print(mid)
    midPoint = xPoints[mid]
    dist_left = minimalDistance(xPoints, yPoints, left, mid)
    dist_right = minimalDistance(xPoints, yPoints, mid+1, right)
    dist_min = min(dist_left, dist_right)
    strip = []
    for i in range(left, right):
        if abs(xPoints[i].x - midPoint.x) < dist_min:
            strip.append(xPoints[i])

    return min(dist_min, stripClosest(strip, dist_min))


def stripClosest(strip, dist_min):
  strip.sort(key = lambda p: p.y)
  min = dist_min
  for i in range(len(strip)):
    for j in range(i+1, len(strip)):
      if strip[j].y - strip[i].y >= min:
        break

      if distance(strip[i], strip[j]) < min:
        min = distance(strip[i], strip[j])

  return min



if __name__ == '__main__':
    n = int(input())
    xPoints = []
    yPoints = []

    for i in range(n):
        x, y = map(float, input().split())
        p = Point(x, y)
        xPoints.append(p)
        yPoints.append(p)

    xPoints.sort(key = lambda p: p.x)
    yPoints.sort(key = lambda p: p.y)

    result = minimalDistance(xPoints, yPoints, 0, n)
    print('{:.2f}'.format(result))
