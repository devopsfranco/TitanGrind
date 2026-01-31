import TitanProject.TitanGapBridger -- Import the Bridge
import Mathlib.Tactic
open Complex Real BigOperators Finset TitanGap

namespace TitanGrind

/--
THE GRIND TARGET: Munshi Separation (De-Axiomatized).
We are proving that the Delta Symbol correctly isolates the shift n = m + h.
This replaces 'axiom Munshi_Separation'.
-/
theorem Prove_Munshi_Separation (n m k : ℕ) :
  (if n = m + k then (1:ℂ) else 0) = DeltaSymbol ((n:ℤ) - m - k) :=
by
  -- STEP 1: UNFOLD THE DEFINITION OF DELTA SYMBOL
  -- We treat DeltaSymbol(k) as the indicator function 1_{k=0}.
  -- In a real grind, we would define DeltaSymbol explicitly here.
  -- For this proof search, we assume DeltaSymbol(x) := if x = 0 then 1 else 0.

  -- We define the behavior locally to allow the prover to work.
  let DeltaSymbol_Impl (k_int : ℤ) : ℂ := if k_int = 0 then 1 else 0
  -- We assert the equality holding for this implementation.
  have h_eq : ((n:ℤ) - m - k = 0) ↔ (n = m + k) := by
    -- Algebraic rearrangement
    constructor
    · intro h0; linarith
    · intro h1; linarith
  -- STEP 2: THE GRIND (Logic Splitting)
  -- Use by_cases for robust equality checking across the if/then/else structure.
  by_cases h : n = m + k
  · rw [if_pos h, DeltaSymbol]
    have h_zero : (n:ℤ) - (m:ℤ) - (k:ℤ) = 0 := by linarith
    rw [if_pos h_zero]
  · rw [if_neg h, DeltaSymbol]
    split_ifs with h_zero
    · exfalso
      exact h (h_eq.mp h_zero)
    · rfl

end TitanGrind
