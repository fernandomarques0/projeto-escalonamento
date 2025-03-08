

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
  
    print(time, cpu, queue, tres, tret)
    time = time + 1
  
  if cpu is not None:
    tret = tret + (endTime - cpu[0])

  print("Tres: ", tres/4)
  print("Tret: ", tret/4)
  print("Tesp: ", tesp/4)

def rr(listOfProcesses):
    time = 0
    queue = []
    cpu = None
    tres = 0
    tret = 0
    tesp = 0
    nProcesses = len(listOfProcesses)
    quantum = 2

    burst_time = {i: p[1] for i, p in enumerate(listOfProcesses)}  # Tempo original de cada processo
    remaining_time = {i: p[1] for i, p in enumerate(listOfProcesses)}  # Tempo restante de execução
    end_time = {}  # Tempo de término de cada processo

    process_list = [p[:] for p in listOfProcesses]  # Criando uma cópia da lista original

    while len(end_time) < len(listOfProcesses):  # Enquanto houver processos não finalizados
        for i, p in enumerate(process_list):
            if p[0] == time:
                queue.append(i)

        if cpu is not None:
            quantum -= 1
            remaining_time[cpu] -= 1

            if remaining_time[cpu] == 0:  # Processo finalizou
                end_time[cpu] = time + 1
                tret += end_time[cpu] - listOfProcesses[cpu][0]  # Calcula Tret
                cpu = None
                quantum = 2

            elif quantum == 0:  # Quantum expirou
                queue.append(cpu)
                cpu = None
                quantum = 2

        if cpu is None and queue:
            cpu = queue.pop(0)
            quantum = 2

        time += 1  # Avança o tempo global

    # Cálculo correto do tempo de espera (Tesp)
    for i in range(len(listOfProcesses)):
        Tret = end_time[i] - listOfProcesses[i][0]  # Tempo de retorno do processo
        Tburst = burst_time[i]  # Tempo original de execução
        Tesp = Tret - Tburst  # Tempo de espera
        tesp += Tesp  # Soma total dos tempos de espera

    # Exibe apenas o tempo de espera médio
    print("Tesp médio:", (tesp / len(listOfProcesses))-1)

if __name__ == "__main__":
  main()