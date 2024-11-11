print("P     Q     P and Q    P or Q    P → Q    P ↔ Q")
print("-" * 45)
for P in [True, False]:
    for Q in [True, False]:
        print(f"{P:<5} {Q:<5} {P and Q:<10} {P or Q:<10} {P <= Q:<8} {P == Q}")