import random
question_data = [
    {
        "text": "A slug's blood is green.",
        "answer": "True"
    },
    {
        "text": "The Earth is flat.",
        "answer": "False"
    },
    {
        "text": "Water boils at 100 degrees Celsius at sea level.",
        "answer": "True"
    },
    {
        "text": "Bananas grow on trees.",
        "answer": "False"
    },
    {
        "text": "Humans have five senses.",
        "answer": "False"
    },
    {
        "text": "Diamonds are formed from coal.",
        "answer": "False"
    },
    {
        "text": "Spiders are insects.",
        "answer": "False"
    },
    {
        "text": "The capital of France is Madrid.",
        "answer": "False"
    },
    {
        "text": "Mars is the closest planet to the Sun.",
        "answer": "False"
    },
    {
        "text": "Rivers always flow from north to south.",
        "answer": "False"
    },
    {
        "text": "Cats are nocturnal animals.",
        "answer": "True"
    },
    {
        "text": "The Great Wall of China is visible from space.",
        "answer": "False"
    },
    {
        "text": "Antibiotics work against viruses.",
        "answer": "False"
    },
    {
        "text": "The chemical symbol for gold is Ag.",
        "answer": "False"
    },
     {
        "text": "Penguins can fly.",
        "answer": "False"
    },
    {
        "text": "The Amazon River is the longest river in the world.",
        "answer": "True"
    },
    {
        "text": "The largest planet in our solar system is Jupiter.",
        "answer": "True"
    },
    {
        "text": "Honey is made from the nectar of flowers.",
        "answer": "True"
    },
    {
        "text": "The chemical symbol for helium is He.",
        "answer": "True"
    },
    {
        "text": "The Moon has its own light source.",
        "answer": "False"
    },
    {
        "text": "Cheetahs are the fastest land animals.",
        "answer": "True"
    },
    {
        "text": "A decagon has eight sides.",
        "answer": "False"
    },
    {
        "text": "The Statue of Liberty was a gift from France to the USA.",
        "answer": "True"
    },
    {
        "text": "Kangaroos are native to South America.",
        "answer": "False"
    },
    {
        "text": "The currency used in India is the Rupee.",
        "answer": "True"
    },
    {
        "text": "The chemical symbol for carbon is Co.",
        "answer": "False"
    },
    {
        "text": "The human body has 206 bones on average.",
        "answer": "True"
    },
    {
        "text": "Mount Kilimanjaro is the tallest mountain in Africa.",
        "answer": "True"
    },
    {
        "text": "Jellyfish are made of 95% water.",
        "answer": "True"
    },
    {
        "text": "The world's largest ocean is the Atlantic Ocean.",
        "answer": "False"
    },
    {
        "text": "Venus is the hottest planet in our solar system.",
        "answer": "True"
    },
    {
        "text": "A group of owls is called a parliament.",
        "answer": "True"
    },
    {
        "text": "The chemical symbol for potassium is Po.",
        "answer": "False"
    },
    {
        "text": "A day on Mars is shorter than a day on Earth.",
        "answer": "True"
    }
]    
random.shuffle(question_data)