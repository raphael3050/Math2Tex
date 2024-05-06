# Math2Tex

Ce projet de compilation a pour but de simplifier la rédaction d'expressions mathématiques Latex en fournissant un outil de conversion d'expressions mathématiques écrites en langage dit 'simplifié' en code Latex. La syntaxe simplifiée s'inspire de la syntaxe des expressions mathématiques en Python, avec peut de caractères spéciaux et une syntaxe claire et concise.

La description du projet ainsi que la grammaire du langage simplifié sont détaillées dans le document `Compilation_Math2Tex.pdf`.

## Important

Ce projet n'inclus pas la syntaxe mathématique complète de Latex, mais seulement les composants les plus couramment utilisés. Il est donc possible que certaines expressions mathématiques ne puissent pas être compilées correctement.

## Utilisation

La première étape avant de pouvoir utiliser le compilateur est d'installer les différentes dépendances nécessaires. Pour cela, il suffit de lancer la commande suivante :

```bash
pip install -r requirements.txt
```

Ensuite, il suffit de lancer le compilateur en lui passant en argument le chemin du fichier contenant l'expression mathématique à compiler. Par exemple :

```bash
python3 -m mathtotex examples/example1.txt
```

Le code Latex généré sera alors affiché dans la console.

## Exemples

Voici quelques exemples d'expressions mathématiques écrites en code Latex et leur équivalent en code simplifié :

##### Puissance
```latex
2^{x+3}
```
```bash
pow(2, x+3)
```

##### Somme
```latex
\sum_{i=0}^{n} 2n
```
```bash
sum(i:0, n, 2n)
```

##### Intégrale
```latex
\int_{a}^{b}{x^2} dx
```
```bash
int(a, b, pow(x, 2), dx)
```


<object data="/examples/ast_example.pdf" type="application/pdf" width="100%"> 
</object>