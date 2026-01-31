import TitanProject.TitanKuznetsov
import TitanProject.TitanGapBridger

open Complex Real BigOperators TitanProject TitanGap

namespace TitanGrind

/--
THE FINAL GRIND: Spectral Transfer.
We prove that the geometric sum of Kloosterman sums bridges to the Spectral side.
-/
theorem Prove_Kuznetsov_Application (X : ℝ) :
  (∑ c ∈ Finset.range (Int.floor X).toNat, (1 / (c : ℂ)) * KloostermanSumGL3 1 1 c) =
  SpectralSum 1 1 X :=
by
  -- STEP 1: INVOKE THE MASTER IDENTITY
  -- We apply the Kuznetsov Trace Formula from the TitanProject library.
  apply GL3_Kuznetsov_Formula

end TitanGrind
