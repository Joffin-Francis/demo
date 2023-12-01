# Maximum power transfer calculator

E=float(input("Please enter the source voltage:"))
Ri=float(input("Please enter the source resistance:"))
Rstart=float(input("Please enter the initial load resistance:"))
Rstop=float(input("Please enter final load resistance:"))
Rfactor=float(input("Please enter the resistance increment factor:"))

if(Rfactor<=1.0):
            Rfactor=2.0

Pmax=(0.5*E)**2/Ri

print("\n\nRload (ohms)\tPload (watts\tEffienciency(%)\n")

Rload=Rstart

while(Rload<=Rstop):
                Vload=E*Rload/(Rload+Ri)
                Pload=Vload**2/Rload
                Ptotal=E**2/(Rload+Ri)
                Eff=100.0*Pload/Ptotal
                print("%-15.8g %-15.8g %-15.8g" %(Rload,Pload,Eff))
                Rload=Rload * Rfactor

print("\nMaximum load power is", Pmax, "watts at",Ri,"ohms\n")
