import hashlib

class ISO50:

  current_file = ''

  def __init__(self, logfile):
    self.logfile = logfile

  def md5_for_file(self, block_size=2**20):
    self.current_file.seek(0)
    md5 = hashlib.new('md5')
    while True:
      data = f.read(block_size)
      if not data:
        break
      md5.update(data)
      return md5.hexdigest()


def main ():
  f = open('input_file.txt', 'rb')
  print f.read()
  print "md5 = %s" % md5_for_file(f)

if __name__== "__main__":
  main()
