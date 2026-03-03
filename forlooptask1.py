total_jump=0;
for i in range(1, 11):
    print("Do 10 jumping jacks")
    total_jump += 10
    print("total completed:", total_jump)

    tired = input("Are u tired(yes/no):")
    if tired == "yes" or tired == "y":
        skip = input("do u want to skip the remaining session?(yes/no):")
        if skip == "yes" or skip == "y":
            print("you completed total of", total_jump, "jumping jacks")
            break  # This needs to be indented further to the right!
            