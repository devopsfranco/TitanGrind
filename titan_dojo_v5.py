"""
TITAN DOJO V5: The Spectral Drill
Target: Kuznetsov Trace Formula (Spectral Transfer)
Context: Phase 3 (Final Pillar)
"""

import sys
import os
import tempfile
from lean_dojo import *

def engage_spectral_grind():
    print("\n[*] TITAN PROTOCOL: ENGAGING SPECTRAL GRIND...")
    
    # 1. Safe Workspace Protocol
    repo_path = os.path.abspath("/Users/franco/dev/Untitled")
    safe_dir = tempfile.mkdtemp()
    os.chdir(safe_dir)
    print(f"    - Execution moved to safe workspace: {safe_dir}")

    # Use LeanGitRepo.from_path for the local project.
    repo = LeanGitRepo.from_path(repo_path)
    
    # 2. Define the Spectral Target
    targets = [
        ("TitanGrind_Spectral.lean", "TitanGrind.Prove_Kuznetsov_Application")
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
            
        print("        [+] Target Locked. Deploying spectral tactics...")
        
        # 3. Search Strategy: SPECTRAL THEORY
        search_result = dojo.search(
            theorem,
            algorithm="best_first",
            max_steps=20000,
            model="reprover-v2-mathlib4",
            hints=[
                "simp",
                "apply GL3_Kuznetsov_Formula", # Core bridge
                "rw [SpectralSide]", 
                "rw [GeometricSide]",
                "unfold SpectralSum",
                "norm_num",
                "ring_nf"
            ]
        )
        
        # 4. Result Handling
        if search_result.status == "proven":
            print(f"        [***] PILLAR SECURED: Proof found for {theorem_name}!")
            print(f"        [***] TACTIC SCRIPT:\n{search_result.proof}")
        else:
            print(f"        [-] DRILL FAILED: {search_result.status}.")

if __name__ == "__main__":
    engage_spectral_grind()
