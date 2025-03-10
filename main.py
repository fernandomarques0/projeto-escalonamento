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
  sjf(listOfProcesses)
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

def sjf(listOfProcesses):
  
  originalValues = [p[:] for p in listOfProcesses]
  time = 0
  prontos = []      
  cpu = None        
  nProcesses = len(listOfProcesses)
  totalProcesses = nProcesses  
  
  tres = 0
  tret = 0
  tesp = 0

  for i in range(len(originalValues)):
    originalValues[i].append(0)  

  while nProcesses > 0:
      if cpu is not None and cpu[1] == 0:
        endtime = time
        tret = tret + (endtime - cpu[0])
        originalValues.remove(cpu)
        if cpu in prontos:
          prontos.remove(cpu)
        nProcesses -= 1
        cpu = None

      for x in originalValues:
        if x[0] == time:
            prontos.append(x)

      prontos.sort(key=lambda p: (p[1], p[0])) 

      if cpu is None and prontos:
        if prontos[0][2] == 0:
          prontos[0][2] = 1
          tres = tres + (time - prontos[0][0])
        cpu = prontos[0]
      
      if cpu is not None:
        cpu[1] -= 1
      
      for p in prontos:
        if p != cpu:
          tesp += 1

      time += 1

  tresMedio = tres / totalProcesses
  tretMedio = tret / totalProcesses
  tespMedio = tesp / totalProcesses

  print("SJF", round(tretMedio, 1), round(tresMedio, 1), round(tespMedio, 1))

def rr(listOfProcesses):

  originalValues = [p[:] for p in listOfProcesses]
  time = 0
  queue = []
  cpu = None
  tres = 0  
  tret = 0  
  tesp = 0  
  nProcesses = len(listOfProcesses)
  totalProcesses = nProcesses
  quantum = 2

  while nProcesses > 0:
      for x in originalValues:
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