

def main():
  listOfProcesses = []
  x = []

  file = open("processos.txt", "r")
  line = file.readline()
  while line != "":
    x.append(list(map(int, line.split())))
    line = file.readline()
  for i in x:
    listOfProcesses.append(i)
  print(listOfProcesses)
  file.close()

  fcfs(listOfProcesses)

def fcfs(listOfProcesses):
  time = 0
  queue = []
  cpu = None
  tres = 0
  tret = 0
  nProcesses = len(listOfProcesses)

  while nProcesses > 0:
    for x in listOfProcesses:
      if x[0] == time:
        if cpu is not None:
          queue.append(x)
        else:
          cpu = x
          startTime = time
          endTime = startTime + cpu[1]
          tres = tres + (startTime - cpu[0])
          nProcesses = nProcesses - 1

    if cpu is not None and time == endTime:
      tret = tret + (endTime - cpu[0])
      cpu = None

      if queue:
        cpu = queue.pop(0)
        startTime = time
        endTime = startTime + cpu[1]
        tres = tres + (startTime - cpu[0])
        nProcesses = nProcesses - 1
  
    print(time, cpu, queue, tres, tret)
    time = time + 1
  
  if cpu is not None:
    tret = tret + (endTime - cpu[0])

  print("Tres: ", tres/4)
  print("Tret: ", tret/4)


if __name__ == "__main__":
  main()