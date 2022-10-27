#define Lamp 8
#define Porta 7

void setup() {
Serial.begin(9600);
pin.Mode(LAMP, OUTPUT);
pin.Mode(PORTA, OUTPUT);

Serial.println("Digite 'L' para ligar a lâmpada e 'l' para desligar");
Serial.println("Digite 'P' para abrir o portão e 'p' para fechar");

}

void loop () {
if (Serial.avalible() ){

    char entrada = Serial.read();

    if (entrada == 'L') {
    digitalWrite (LAMP, HIGH);
    } else if (entrada == 'l') {
    digitalWrite (LAMP,LOW);
    }

    if (entrada == 'P') {
    digitalWrite (PORTA, HIGH);
    }   else if (entrada == 'p'){
    digitalWrite (PORTA,LOW);
    }

}

}