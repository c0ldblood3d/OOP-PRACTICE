from OnlineBank import OnlineBank

ob = OnlineBank()
ob.register_account("ONB-501", 1500)
ob.register_account("ONB-502", 600)
ob.deposit_funds("ONB-501", 200)
ob.withdraw_funds("ONB-502", 250)
ob.check_current_balance("ONB-501")
ob.check_current_balance("ONB-502")
ob.withdraw_funds("ONB-502", 400) 
ob.check_current_balance("ONB-999") 
