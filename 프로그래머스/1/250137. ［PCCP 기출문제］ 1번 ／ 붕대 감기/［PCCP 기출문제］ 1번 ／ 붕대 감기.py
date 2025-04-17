def solution(bandage, health, attacks):
    banding_sec, heal_per_sec, heal_bonus = bandage
    current_health = health
    
    sec = 1
    for attack_sec, attack_power in attacks:        
        if sec == attack_sec:
            current_health -= attack_power
            sec += 1
            if current_health <= 0:
                return -1
            continue
        
        heal_bonus_sec = 1
        # sec는 계속 늘어남 -> attack_sec와 비교
        while sec < attack_sec:
            if heal_bonus_sec % banding_sec == 0:
                current_health += heal_bonus
                if current_health > health:
                    current_health = health
            
            if current_health < health:
                current_health += heal_per_sec
                if current_health > health:
                    current_health = health
            
            heal_bonus_sec += 1
            sec += 1
        
        current_health -= attack_power
        sec += 1
        if current_health <= 0:
            return -1

            
    return current_health