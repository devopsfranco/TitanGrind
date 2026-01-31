"""
TITAN DOJO V3: The Precision Grind
Target: Munshi Separation Identity (Combinatorics)
Context: Phase 3 De-Axiomatization
"""

import sys
import numpy as np
from lean_dojo import *

def engage_precision_grind():
    # 1. Initialize the Environment
    print("\n[*] TITAN PROTOCOL: ENGAGING PRECISION GRIND (COMBINATORICS)...")
    import os
    import tempfile
    
    # We move to a temporary directory to avoid the FileExistsError.
    # LeanDojo tries to copy the project to a folder named 'Untitled' in the CWD.
    repo_path = os.path.abspath("/Users/franco/dev/Untitled")
    safe_dir = tempfile.mkdtemp()
    os.chdir(safe_dir)
    print(f"    - Execution moved to safe workspace: {safe_dir}")
    
    repo = LeanGitRepo.from_path(repo_path)
    
    # 2. Define the Precision Target
    # We are no longer scanning the whole bridge. We are attacking one tile.
    targets = [
        ("TitanGrind_Combinatorics.lean", "TitanGrind.Prove_Munshi_Separation")
    ]
    
    # 3. The Grind Loop
    for filename, theorem_name in targets:
        print(f"\n    [>] DRILLING TARGET: {theorem_name}...")
        
        # Trace the specific file
        traced_file = trace(repo, filename)
        theorem = next((t for t in traced_file.get_traced_theorems() 
                       if t.full_name == theorem_name), None)
        
        if not theorem:
            print(f"        [!] Error: Target {theorem_name} not found. Check Lean file.")
            continue
            
        print("        [+] Target Locked. deploying algebraic tactics...")
        
        # 4. Search Strategy (Algebraic Focus)
        # We explicitly hint tactics that solve sums and equalities.
        search_result = dojo.search(
            theorem,
            algorithm="best_first",
            max_steps=10000,         # Deep drill
            model="reprover-v2-mathlib4",
            hints=[
                "simp",              # Simplification
                "ring",              # Algebraic Ring Solver (Crucial for Delta Method)
                "rw [Finset.sum_ite]", # Split sums based on if/then
                "congr",             # Logic congruence
                "apply Iff.intro"    # Logic splitting
            ]
        )
        
        # 5. Result Handling
        if search_result.status == "proven":
            print(f"        [***] AXIOM DESTROYED: Proof found for {theorem_name}!")
            print(f"        [***] INJECT THIS TACTIC SCRIPT:\n{search_result.proof}")
        else:
            print(f"        [-] DRILL FAILED: {search_result.status}. Try manual decomposition.")

if __name__ == "__main__":
    engage_precision_grind()