def main():
    print("Hackathon Team Formation and Ranking")

    min_team_size = int(input("Minimum team size: "))
    max_team_size = int(input("Maximum team size: "))
    round_count = int(input("Number of scoring rounds: "))
    team_count = int(input("Number of teams: "))

    if min_team_size <= 0 or max_team_size < min_team_size:
        print("Error: Invalid team size limits.")
        return
    if round_count <= 0 or team_count <= 0:
        print("Error: Round count and team count must be positive.")
        return

    valid_teams = []
    invalid_teams = []

    for team_index in range(team_count):
        print(f"\nTeam {team_index + 1}")
        team_name = input("Team name: ").strip()
        member_count = int(input("Number of team members: "))

        if member_count < 0:
            print("Error: Member count cannot be negative.")
            return

        members = []
        for member_index in range(member_count):
            member_name = input(f"Member {member_index + 1} name: ").strip()
            scores = []

            for round_index in range(round_count):
                score = float(
                    input(f"{member_name} score in Round {round_index + 1}: ")
                )
                if score < 0:
                    print("Error: Scores cannot be negative.")
                    return
                scores.append(score)

            members.append({"name": member_name, "scores": scores})

        if not min_team_size <= member_count <= max_team_size:
            invalid_teams.append((team_name, member_count))
            continue

        round_totals = [
            sum(member["scores"][round_index] for member in members)
            for round_index in range(round_count)
        ]

        valid_teams.append({
            "name": team_name,
            "members": members,
            "round_totals": round_totals,
            "total": sum(round_totals),
        })

    # Sort by total score, then final round, then earlier rounds (latest first),
    # then team name alphabetically.
    valid_teams.sort(
        key=lambda team: (
            -team["total"],
            *(-score for score in reversed(team["round_totals"])),
            team["name"].casefold(),
        )
    )

    print("\nInvalid Teams")
    if invalid_teams:
        for name, size in invalid_teams:
            print(
                f"{name}: {size} members "
                f"(allowed size: {min_team_size}-{max_team_size})"
            )
    else:
        print("None")

    print("\nTeam Rankings")
    if not valid_teams:
        print("No valid teams to rank.")
        return

    for rank, team in enumerate(valid_teams, start=1):
        rounds = ", ".join(
            f"Round {index + 1}: {score:g}"
            for index, score in enumerate(team["round_totals"])
        )
        print(
            f"{rank}. {team['name']} | Total: {team['total']:g} | "
            f"{rounds}"
        )


if __name__ == "__main__":
    main()
