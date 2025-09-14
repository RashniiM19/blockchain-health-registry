from pyteal import *


BIRTH_REGISTRY_MAP = Bytes("birth_records")

def approval_program():

    on_creation = Seq([
        App.globalPut(BIRTH_REGISTRY_MAP, Bytes("")),  # Initialize a global key (optional)
        Return(Int(1))
    ])

 
    register_birth = Seq([
       
        Assert(App.localGet(Int(0), Txn.application_args[1]) == Int(0)),
        
     
        App.globalPut(Txn.application_args[1], Txn.application_args[2]),
        
   
        Log(Concat(Bytes("BirthRegistered"), Txn.application_args[1])),
        
        Return(Int(1))
    ])


    program = Cond(
        [Txn.application_id() == Int(0), on_creation],
        [Txn.on_completion() == OnComplete.NoOp, Cond(
            [Txn.application_args[0] == Bytes("register_birth"), register_birth],
        )],
        # Allow the application to be closed or deleted by its creator
        [Txn.on_completion() == OnComplete.DeleteApplication, Return(Int(1))],
        [Txn.on_completion() == OnComplete.UpdateApplication, Return(Int(1))],
        [Txn.on_completion() == OnComplete.OptIn, Return(Int(1))]
    )
    
    return compileTeal(program, Mode.Application, version=6)

# This is a dummy clear state program, mandatory for an Algorand smart contract
def clear_state_program():
    return Return(Int(1))

if __name__ == "__main__":
    with open("BirthRegistry.teal", "w") as f:
        compiled_teal = approval_program()
        f.write(compiled_teal)