# MacPmem.kext를 찾는 명령어 >> sudo find / -name MacPmem.kext 2>/dev/null

import subprocess
import os

def capture_memory_dump(kext_path):
    # 'mac_result' 폴더 생성 혹은 확인
    results_folder = 'mac_result'
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    # 결과값 저장 경로를 'mac_result' 폴더 내로 지정
    output_path = os.path.join(os.getcwd(), results_folder, "memory_dump.raw")
    
    # MacPmem의 kext를 로드합니다.
    kextload_cmd = ["sudo", "kextload", kext_path]
    subprocess.run(kextload_cmd, check=True)
    
    # 메모리 덤프를 캡처합니다.
    dump_cmd = ["sudo", "dd", "if=/dev/pmem", f"of={output_path}", "bs=2M"]
    subprocess.run(dump_cmd, check=True)
    
    # MacPmem의 kext를 언로드합니다.
    kextunload_cmd = ["sudo", "kextunload", kext_path]
    subprocess.run(kextunload_cmd, check=True)

    print(f"Memory dump saved to {output_path}")


kext_path = "절대경로 투입/MacPmem.kext"
capture_memory_dump(kext_path)
