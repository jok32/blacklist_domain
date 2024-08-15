import cdblib
import blocklist_aggregator
import time

def save_raw():
    start_time = time.time()
    fn = "/etc/dnsdist/conf.d/blocklist_raw.txt"
    blocklist_aggregator.save_raw(filename=fn)
    elapsed_time = time.time() - start_time
    print(f"save raw blocklist completed successfully. Time taken: {elapsed_time:.2f} seconds")

def save_hosts():
    start_time = time.time()
    fn = "/etc/dnsdist/conf.d/hosts.txt"
    blocklist_aggregator.save_hosts(filename=fn, ip="103.30.181.1")
    elapsed_time = time.time() - start_time
    print(f"save hosts blocklist completed successfully. Time taken: {elapsed_time:.2f} seconds")

def save_cdb():
    start_time = time.time()
    fn = "/etc/dnsdist/conf.d/blocklist.cdb"
    blocklist_aggregator.save_cdb(filename=fn)
    elapsed_time = time.time() - start_time
    print(f"save cdb blocklist completed successfully. Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    save_raw()
    save_hosts()
    save_cdb()
