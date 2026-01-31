"""
TITAN DOJO V4: The Analytic Drill
Target: Bessel Decay (Analysis)
Context: Phase 3 De-Axiomatization
"""

import sys
import os
import tempfile
from lean_dojo import *

def engage_analytic_grind():
    print("\n[*] TITAN PROTOCOL: ENGAGING ANALYTIC GRIND...")
    
    # 1. Safe Workspace Protocol
    # We move to a temporary directory to avoid the FileExistsError.
    # LeanDojo tries to copy the project to a folder named 'Untitled' in the CWD.
    repo_path = os.path.abspath("/Users/franco/dev/Untitled")
    safe_dir = tempfile.mkdtemp()
    os.chdir(safe_dir)
    print(f"    - Execution moved to safe workspace: {safe_dir}")

    # Use LeanGitRepo.from_path for the local project.
    repo = LeanGitRepo.from_path(repo_path)
    
    # 2. Define the Analytic Target
    targets = [
        ("TitanGrind_Analysis.lean", "TitanGrind.Prove_Bessel_Decay")
    ]
    
    for filename, theorem_name in targets:
        print(f"\n    [>] DRILLING TARGET: {theorem_name}...")
        
        # Trace the specific file
        traced_file = trace(repo, filename)
        theorem = next((t for t in traced_file.get_traced_theorems() 
                       if t.full_name == theorem_name), None)
        
        if not theorem:
            print(f"        [!] Error: Target {theorem_name} not found.")
            continue
            
        print("        [+] Target Locked. Deploying analysis tactics...")
        
        # 3. Search Strategy: ANALYSIS
        # We assume the user has cloned mathlib (overhead complete).
        search_result = dojo.search(
            theorem,
            algorithm="best_first",
            max_steps=20000,         # Deeper search for calculus
            model="reprover-v2-mathlib4",
            hints=[
                "simp",
                "norm_num",          # Crucial for trig identities
                "rw [Complex.exp_re]",
                "rw [Complex.exp_im]",
                "rw [Complex.log_re]",
                "apply Complex.ext", # Extensionality for complex numbers
                "ring_nf"            # Normal form ring solver
            ]
        )
        
        # 4. Result Handling
        if search_result.status == "proven":
            print(f"        [***] AXIOM DESTROYED: Proof found for {theorem_name}!")
            print(f"        [***] TACTIC SCRIPT:\n{search_result.proof}")
        else:
            print(f"        [-] DRILL FAILED: {search_result.status}.")

if __name__ == "__main__":
    engage_analytic_grind()
