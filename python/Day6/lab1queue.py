class Queue:                               # Queue is class name
  def __init__(self):
      self.queue = list()                  # queue is an instance variable
  def addToQueue(self,value):
# Insert method to add element
      if value not in self.queue:
          self.queue.insert(0,value)
          return True
      return False
  def size(self):
      return len(self.queue)
MySuperHero = Queue()
MySuperHero.addToQueue("Thor")
MySuperHero.addToQueue("Iron man")
MySuperHero.addToQueue("Hulk")
MySuperHero.addToQueue("Doctor Strange")
MySuperHero.addToQueue("Vision")
MySuperHero.addToQueue("captain america")
print(MySuperHero.size())