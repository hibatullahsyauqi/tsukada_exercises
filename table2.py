print("P     Q     P and Q    P or Q    P → Q    P ↔ Q")
print("-" * 45)
for P in [True, False]:
    for Q in [True, False]:
        print(f"{str(P):<5} {str(Q):<5} {str(P and Q):<10} {str(P or Q):<10} {str(P <= Q):<8} {str(P == Q)}")
