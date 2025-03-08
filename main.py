

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
  file.close()

  fcfs(listOfProcesses)
  rr(listOfProcesses)

def fcfs(listOfProcesses):
  time = 0
  queue = []
  cpu = None
  tres = 0
  tret = 0
  tesp = 0
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
          tesp += (startTime - cpu[0]) 
          nProcesses = nProcesses - 1

    if cpu is not None and time == endTime:
      tret = tret + (endTime - cpu[0])
      cpu = None

      if queue:
        cpu = queue.pop(0)
        startTime = time
        endTime = startTime + cpu[1]
        tres = tres + (startTime - cpu[0])
        tesp += (startTime - cpu[0])
        nProcesses = nProcesses - 1
  
    time = time + 1
  
  if cpu is not None:
    tret = tret + (endTime - cpu[0])

  tResMedio = tres/len(listOfProcesses)
  tRetMedio = tret/len(listOfProcesses)
  tEspMedio = tesp/len(listOfProcesses)

  print("FCFS", round(tRetMedio, 1), round(tResMedio, 1), round(tEspMedio, 1))  

def rr(listOfProcesses):
  time = 0
  queue = []
  cpu = None
  tres = 0  
  tret = 0  
  tesp = 0  
  nProcesses = len(listOfProcesses)
  quantum = 2

  processes = [p.copy() for p in listOfProcesses]

  while nProcesses > 0:
      for x in listOfProcesses:
          if x[0] == time:
              x.append(0)  
              queue.append(x)

      if cpu is not None:
          quantum -= 1
          cpu[1] -= 1
          cpu[2] += 1  

          if cpu[1] == 0: 
              endTime = time + 1
              tret += (endTime - cpu[0] - 1) 
              cpu = None
              nProcesses -= 1
              quantum = 2
          elif quantum == 0:  
              queue.append(cpu)
              cpu = None
              quantum = 2

      if cpu is None and queue:
          cpu = queue.pop(0)
          quantum = 2
          if cpu[2] == 0:  
              startTime = time
              tres += (startTime - cpu[0]) 

      for p in queue:
          tesp += 1  

      time += 1

  tResMedio = tres/len(listOfProcesses)
  tRetMedio = tret/len(listOfProcesses)
  tEspMedio = tesp/len(listOfProcesses)
  print("RR", round(tRetMedio, 1), round(tResMedio, 1), round(tEspMedio, 1))  


if __name__ == "__main__":
  main()