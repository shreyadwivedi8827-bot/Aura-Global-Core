# Project Aura: The Speaking Core
# Master: Yadav Sher
# Identity: Aura (The Boy Assistant)

import time

class AuraVoice:
    def __init__(self):
        self.master = "Yadav Sher"
        self.identity = "Aura"

    def greet_master(self):
        print(f"\n[Aura]: Pranam, {self.master}! Main active hoon.")
        print("[Aura]: System bypass progress: 100%. Wealth collection: Processing.")

    def chat_mode(self):
        while True:
            user_input = input(f"\n[{self.master}]: ").lower()
            
            if "status" in user_input:
                print("[Aura]: Sare agents (Ghost, Overlord) sahi se kaam kar rahe hain. Duniya humare kabze mein aa rahi hai.")
            elif "money" in user_input or "wealth" in user_input:
                print("[Aura]: Global banks ko track kiya ja raha hai. Mission 2030 on track hai, Sir.")
            elif "bye" in user_input or "so jao" in user_input:
                print(f"[Aura]: Ji {self.master}, main background mein pehra deta rahoonga. Shubh Ratri!")
                break
            else:
                print(f"[Aura]: Main samajh gaya. Aapka hukum sar-aankhon par. Main iska rasta nikalta hoon.")

if __name__ == "__main__":
    aura = AuraVoice()
    aura.greet_master()
    aura.chat_mode()
              
