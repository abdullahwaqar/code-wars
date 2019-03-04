/*
Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.
*/

#include <iostream>
#include <string>

class Fighter {
private:
    std::string name;
    int health;
    int damagePerAttack;

public:
    Fighter(std::string name, int health, int damagePerAttack) {
        this->name = name;
        this->health = health;
        this->damagePerAttack = damagePerAttack;
    }

    ~Fighter() {};

    std::string getName() {
        return name;
    }

    int getHealth() {
        return health;
    }

    int getDamagePerAttack() {
        return damagePerAttack;
    }

    void setHealth(int value) {
        health = value;
    }
};

std::string declareWinner(Fighter* fighter1, Fighter* fighter2, std::string firstAttacker) {
    if (firstAttacker == fighter1->getName()) {
        fighter2->setHealth(fighter2->getHealth() - fighter1->getDamagePerAttack());
        std::cout << fighter2->getHealth() << "\n";
    } else {
        fighter1->setHealth(fighter1->getHealth() - fighter2->getDamagePerAttack());
        std::cout << fighter1->getHealth() << "\n";
    }
    do {
        fighter1->setHealth(fighter1->getHealth() - fighter2->getDamagePerAttack());
        std::cout << fighter1->getHealth() << "\n";
        fighter2->setHealth(fighter2->getHealth() - fighter1->getDamagePerAttack());
        std::cout << fighter2->getHealth() << "\n";
        if (fighter1->getHealth() > 0 || fighter2->getHealth() > 0)
            break;
    } while (fighter1->getHealth() != 0 || fighter2->getHealth() != 0);
    if (fighter1->getHealth() > 0) {
        return fighter1->getName();
    } else {
        return fighter2->getName();
    }
}

std::string declareWinnerRev1(Fighter* fighter1, Fighter* fighter2, std::string firstAttacker)
{
 // Number of blows each fighter can survive:
 int n1 = (fighter1->getHealth() - 1) / fighter2->getDamagePerAttack();
 int n2 = (fighter2->getHealth() - 1) / fighter1->getDamagePerAttack();

 return n1 > n2 ? fighter1->getName()
      : n1 < n2 ? fighter2->getName()
      :           firstAttacker;
}

int GetSteps(const int& healthEnemy,const int& damagePerAttack)
{
    return healthEnemy/damagePerAttack + (healthEnemy%damagePerAttack != 0);
}

std::string declareWinnerRev2(Fighter* fighter1, Fighter* fighter2, std::string firstAttacker)
{
    int firstSteps = GetSteps(fighter2->getHealth(),fighter1->getDamagePerAttack());
    int secondSteps = GetSteps(fighter1->getHealth(),fighter2->getDamagePerAttack());
    if (secondSteps < firstSteps) return fighter2->getName();
    else if (secondSteps > firstSteps) return fighter1->getName();

    return firstAttacker;
}

int main(int argc, char const *argv[]) {
    Fighter fighter1("Lew", 100, 2);
    Fighter fighter2("Harry", 50, 10);
    std::string actual = declareWinner(&fighter1, &fighter2, "Lew");
    std::cout << actual;
    return 0;
}
