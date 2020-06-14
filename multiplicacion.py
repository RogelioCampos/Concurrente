from operaciones import suma,mul,resta
import sys
sys.path.append('/usr/lib64/python3.7/site-packages/mpich')
from mpi4py import MPI
comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()
print("%d of%d" % (comm.Get_rank(), comm.Get_size()))

if rank ==0: #root
	A = [[2,3,1,-1],[-2,0,-2,3],[2,3,1,2],[3,4,2,3]]
	B = [[2,1,3,2],[-1,2,-3,0],[1,0,2,0],[-1,0,2,0]]
else:
	A,B = None, None
# envía raiz todos los datos a todos los procesadores
A = comm.bcast(A, root=0)
B = comm.bcast(B, root=0)

A11=[A[0][0:2],A[1][0:2]]
A12=[A[0][2:4],A[1][2:4]]
A21=[A[2][0:2],A[3][0:2]]
A22=[A[2][2:4],A[3][2:4]]

B11=[B[0][0:2],B[1][0:2]]
B12=[B[0][2:4],B[1][2:4]]
B21=[B[2][0:2],B[3][0:2]]
B22=[B[2][2:4],B[3][2:4]]

if rank == 0:
	P1 = mul(suma(A11,A22),suma(B11,B22))
	P2 = mul(suma(A21,A22),B11)
	P6 = comm.recv(source=1, tag=11)
	P3 = mul(A11,resta(B12,B22))
	C22 = suma(resta(suma(P1,P3),P2),P6)
	P5 = comm.recv(source=1, tag=22)
	comm.send(P2,dest=1, tag=33)
	C12 = suma(P3,P5)
	comm.send(P1,dest=1, tag=44)
	C21 = comm.recv(tag=100)
	C11 = comm.recv(tag=110)

elif rank == 1:
	P4 = mul(A22,resta(B21,B11))
	P6 = mul(resta(A21,A11),suma(B11,B12))
	comm.send(P6, dest=0, tag=11)
	P5 = mul(suma(A11,A12),B22)
	P7 = mul(resta(A12,A22),suma(B21,B22))
	comm.send(P5,dest=0, tag=22)
	P2 = comm.recv(source=0, tag=33)
	C21 = suma(P2,P4)
	P1 = comm.recv(source=0, tag=44)
	C11 = suma(resta(suma(P1,P4),P5),P7)
	comm.send(C21,dest=0, tag=100)
	comm.send(C11,dest=0, tag=110)

if rank == 0:
	print('C11-> ',C11)
	print('C12-> ',C12)
	print('C21-> ',C21)
	print('C22-> ',C22)
