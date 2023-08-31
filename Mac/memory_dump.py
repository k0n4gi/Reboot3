#sudo로 실행
#Rekall 오픈소스 사용
#apple Sillicon에서는 사용 불가능
import subprocess
import os

def capture_memory_dump(kext_path):
    output_path = os.path.join(os.getcwd(), "memory_dump.raw")
    
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

# 실행 예제
kext_path = "절대경로 투입/MacPmem.kext"
capture_memory_dump(kext_path)
