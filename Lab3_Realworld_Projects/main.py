import access_control as ac
import media_engine as me

STUDENT_LAST_DIGIT = 3 
FAVORITE_ARTIST = "Daniel Caesar" 

SEED_NUM = STUDENT_LAST_DIGIT
CONTROL_NUM = max(1, SEED_NUM)

def run_mission_1():
    print("--- MISSION 1: AUTHORIZATION PROTOCOL ---")
    level = ac.compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)
    decision = ac.validate_access(level, CONTROL_NUM)
    print(f"Access Level: {level}")
    print(f"Decision: {decision}\n")

def run_mission_2():
    print("--- MISSION 2: RECURSIVE SIGNAL SHUTDOWN ---")
    initial_power = CONTROL_NUM + len(FAVORITE_ARTIST)
    total_calls = me.signal_shutdown(initial_power)
    print(f"Total recursive calls: {total_calls}\n")

def run_mission_3():
    print("--- MISSION 3: STREAMING ANALYTICS ---")
    limit = CONTROL_NUM + len(FAVORITE_ARTIST)
    
    @me.monitor
    def process_analytics():
        total_plays = 0
        records_count = 0
        for value in me.play_count_stream(limit):
            print(f"Generated Play Count: {value}")
            total_plays += value
            records_count += 1
        return total_plays, records_count

    total, count = process_analytics()
    print(f"Total Plays: {total}")
    print(f"Records Processed: {count}\n")

if __name__ == "__main__":
    run_mission_1()
    run_mission_2()
    run_mission_3()