# Verify the first equivalence: P → Q ⇔ ¬P ∨ Q
print("Equivalence 1: P → Q ⇔ ¬P ∨ Q")
for P in [True, False]:
    for Q in [True, False]:
        implication = P <= Q                  # P → Q
        disjunction = (not P) or Q            # ¬P ∨ Q
        assert implication == disjunction, "Equivalence 1 Failed"
        print(f"P: {P}, Q: {Q}, P → Q: {implication}, ¬P ∨ Q: {disjunction} - Match")

# Verify the second equivalence: P ↔ Q ⇔ (P → Q) ∧ (Q → P)
print("\nEquivalence 2: P ↔ Q ⇔ (P → Q) ∧ (Q → P)")
for P in [True, False]:
    for Q in [True, False]:
        biconditional = (P == Q)               # P ↔ Q
        forward_implication = P <= Q           # P → Q
        backward_implication = Q <= P          # Q → P
        conjunction = forward_implication and backward_implication  # (P → Q) ∧ (Q → P)
        assert biconditional == conjunction, "Equivalence 2 Failed"
        print(f"P: {P}, Q: {Q}, P ↔ Q: {biconditional}, (P → Q) ∧ (Q → P): {conjunction} - Match")
