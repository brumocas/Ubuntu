/*****************************************************************/
/*          Grafo direcionado | PROG2 | MIEEC | 2020/21          */
/*****************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "grafo.h"
#include "heap.h"


#define infinity 99999999999999

//----------Funcoes auxiliares para grafo.c--------------------//
/**
 * Imprime destinos apartir de uma cidade (nó)
 * */
void imprime_arestas( no_grafo *no);

//---------Funcoes normais-------------------------------------//

grafo *grafo_novo()
{
    grafo *g = (grafo *)malloc(sizeof(grafo));
    g->tamanho = 0;
    g->nos = NULL;

    return g;
}

no_grafo *encontra_no(grafo *g, char *cidade)
{
    if (!g || !cidade)
        return NULL;

    // pesquisa por cidade no vetor de nós
    for (int i = 0; i < g->tamanho; i++)
    {
        if (strcmp(g->nos[i]->cidade, cidade) == 0)
            return g->nos[i];
    }
    return NULL;
}

no_grafo *no_insere(grafo *g, char *cidade)
{
    if (!g || !cidade)
        return NULL;

    // verifica se o nó já existe
    no_grafo *no = encontra_no(g, cidade);
    if (no)
        return NULL;

    // cria o novo nó para o user
    no = (no_grafo *)malloc(sizeof(no_grafo));
    if (!no)
        return NULL;

    // aloca espaço para o campo cidade
    no->cidade = (char *)malloc((strlen(cidade) + 1) * sizeof(char));
    if (!no->cidade)
    {
        free(no);
        return NULL;
    }
    // inicializa todos os campos
    strcpy(no->cidade, cidade);
    no->tamanho = 0;
    no->arestas = NULL;
    no->p_acumulado = 0;
    no->anterior = NULL;
    no->dataatualizada = NULL;

    // insere o nó criado no final do vetor de nós
    g->nos = (no_grafo **)realloc(g->nos, (g->tamanho + 1) * sizeof(no_grafo *));
    if (!g->nos)
    {
        free(no->cidade);
        free(no);
        return NULL;
    }
    // incrementa o tamanho do numero de nós e insere no vetor de apontadores de nós
    g->tamanho++;
    g->nos[g->tamanho - 1] = no;

    return no;
}

// função auxiliar que retorna 1 se existir a aresta para destino ou 0,
// se a aresta não existir, -1 se der erro
int existe_aresta(no_grafo *origem, no_grafo *destino, char *codigo)
{

    if (!origem || !destino)
        return -1;

    //pesquisa em todas as arestas se existe
    for (int i = 0; i < origem->tamanho; i++)
    {

        if ((origem->arestas[i]->destino == destino) && ((strcmp(origem->arestas[i]->codigo, codigo) == 0)))
            return 1;
    }

    return 0;
}

int cria_aresta(no_grafo *origem, no_grafo *destino, char *codigo, char *companhia, data partida, data chegada, float preco, int lugares)
{
    if (!origem || !destino || !codigo || !companhia)
        return -1;

    if (preco < 0 || lugares < 0)
        return -1;

    // verifica se a ligação já existe
    if (existe_aresta(origem, destino, codigo) > 0)
        return -1;

    // cria a nova ligação
    aresta_grafo *ag = (aresta_grafo *)malloc(sizeof(aresta_grafo));
    if (!ag)
        return -1;

    ag->destino = destino;
    ag->preco = preco;
    ag->lugares = lugares;
    // aloca espaço para o código
    ag->codigo = (char *)malloc((strlen(codigo) + 1) * sizeof(char));
    if (!ag->codigo)
    {
        free(ag);
        return -1;
    }
    strcpy(ag->codigo, codigo);
    // aloca espaço para o companhia
    ag->companhia = (char *)malloc((strlen(companhia) + 1) * sizeof(char));
    if (!ag->companhia)
    {
        free(ag->codigo);
        free(ag);
        return -1;
    }
    strcpy(ag->companhia, companhia);

    // inicializa todos os campos
    ag->partida.tm_year = partida.tm_year;
    ag->partida.tm_mon = partida.tm_mon;
    ag->partida.tm_mday = partida.tm_mday;
    ag->partida.tm_hour = partida.tm_hour;
    ag->partida.tm_min = partida.tm_min;
    ag->partida.tm_sec = 0;
    ag->partida.tm_isdst = 0;  //Horario de verao ou inverno
    
    // inicializa todos os campos
    ag->chegada.tm_year = chegada.tm_year;
    ag->chegada.tm_mon = chegada.tm_mon;
    ag->chegada.tm_mday = chegada.tm_mday;
    ag->chegada.tm_hour = chegada.tm_hour;
    ag->chegada.tm_min = chegada.tm_min;
    ag->chegada.tm_sec = 0;
    ag->chegada.tm_isdst = 0;

    // insere a nova ligação no vetor de ligações
    origem->arestas = (aresta_grafo **)realloc(origem->arestas, (origem->tamanho + 1) * sizeof(aresta_grafo *));
    if (!origem->arestas)
    {
        free(ag->codigo);
        free(ag->companhia);
        free(ag);
        return -1;
    }
    origem->tamanho++;
    origem->arestas[origem->tamanho - 1] = ag;

    return 0;
}
//------------------------------------------Funcoes a implementar começa aqui--------------------------------------------------------------//

no_grafo *no_remove(grafo *g, char *cidade)
{   if(!g || !cidade || g->tamanho < 0 )
    return NULL;
    
    if (!encontra_no(g,cidade))
    return NULL;
    
    
    no_grafo *aux;
    
    for (int i = 0; i < g->tamanho ; i++)
    {  
        for (int k = 0; k < g->nos[i]->tamanho; k++)
        {   
            if (strcmp(g->nos[i]->arestas[k]->destino->cidade,cidade)==0) //remover viagens com destino para a cidade (nó) a remover
            {   
                aresta_grafo *tmp;
                
                tmp=g->nos[i]->arestas[k];
                g->nos[i]->arestas[k]=g->nos[i]->arestas[g->nos[i]->tamanho-1];
                g->nos[i]->arestas[g->nos[i]->tamanho-1]=tmp;

                free(g->nos[i]->arestas[g->nos[i]->tamanho-1]->companhia);
                free(g->nos[i]->arestas[g->nos[i]->tamanho-1]->codigo);
                free(g->nos[i]->arestas[g->nos[i]->tamanho-1]);     
                
                g->nos[i]->arestas = (aresta_grafo **)realloc(g->nos[i]->arestas, (g->nos[i]->tamanho -1 ) * sizeof(aresta_grafo *));
                g->nos[i]->tamanho--;
            }
        }
        
        if (strcmp(g->nos[i]->cidade,cidade)==0)//no a remover encontrado
        {   
            aux=g->nos[i];
            g->nos[i]=g->nos[g->tamanho-1];
            g->nos[g->tamanho-1]=aux;
            g->nos = (no_grafo **)realloc(g->nos, (g->tamanho - 1) * sizeof(no_grafo *));
            g->tamanho--;
        }
        
    }
    return aux;
}

int aresta_apaga(aresta_grafo *aresta)
{   if(!aresta)
    return -1;
     
    free(aresta->codigo);
    free(aresta->companhia);
    free(aresta);

    return 0;
}

int no_apaga(no_grafo *no)
{   if(!no)
    return -1;
    
    for (int i = 0; i < no->tamanho; i++)
    {   
        aresta_apaga(no->arestas[i]);
    }
    
    free(no->arestas);
    free(no->cidade);
    free(no);
    
    return 0;
}

void grafo_apaga(grafo *g)
{   if(!g)
    return;

    for (int i = 0; i < g->tamanho; i++)
    {
        no_apaga(g->nos[i]);
    }
    free(g->nos);
    free(g);
}

no_grafo *encontra_voo(grafo *g, char *codigo, int *aresta_pos)
{   if(!g || !codigo )
    return NULL;
    
    no_grafo *encontrado;

    for (int i = 0; i < g->tamanho; i++)
    {
        for (int k = 0; k < g->nos[i]->tamanho; k++)
        {
            if (strcmp(g->nos[i]->arestas[k]->codigo,codigo)==0)
            {
                encontrado=g->nos[i];
                *aresta_pos=k;
                return encontrado;
            }   
        }     
    }
    *aresta_pos=-1; 
    return NULL;
}

no_grafo **pesquisa_avancada(grafo *g, char *destino, data chegada, double preco_max, int *n)
{   
    if( !g || !destino || preco_max < 0.0 || g->tamanho < 0 || g->nos==NULL || mktime(&chegada) <= 0)
    return NULL;
    

    no_grafo** voo = (no_grafo**) malloc(sizeof(no_grafo*));//memoria para o vetor de voos a devolver
    if(!voo)
    return NULL;

    int existe=0,viagem=0;

    for (int i=0; i<g->tamanho; i++)
    {
        for (int j=0; j< g->nos[i]->tamanho; j++)
        {
            if(strcmp(g->nos[i]->arestas[j]->destino->cidade, destino)==0 && (g->nos[i]->arestas[j]->chegada.tm_mday == chegada.tm_mday && g->nos[i]->arestas[j]->chegada.tm_year == chegada.tm_year && g->nos[i]->arestas[j]->chegada.tm_mon == chegada.tm_mon) && g->nos[i]->arestas[j]->preco <= preco_max)
            {   
                //verificar se cidade (nó) ja existe no vetor a devolver
                existe=0;
                for(int k=0 ; k < viagem ;k++)
                { 
                    //if (strcmp(g->nos[i]->cidade,voo[k]->cidade)==0) outra possibilidade 
                    if (g->nos[i]==voo[k])
                    {
                        existe=1;
                        break;
                    }
                }

                if(existe==0)
                { 
                viagem++;
                voo = (no_grafo**) realloc (voo, viagem*sizeof(no_grafo*));
                voo [viagem-1] = g->nos[i];
                }

            }
        }
    }
    *n = viagem;
    return voo;
}

no_grafo **trajeto_mais_rapido(grafo *g, char *origem, char *destino, data partida, int *n)
{   if(!g || !origem || !destino || mktime(&partida) <= 0 ) 
    return NULL;

  
    return NULL;
}

no_grafo **menos_transbordos(grafo *g, char *origem, char *destino, data partida, int *n)
{   if(!g || !origem || !destino || mktime(&partida) <= 0 ) //comparar data partida
    return NULL;
    
     no_grafo *cidade_origem=encontra_no(g,origem);
    if(!cidade_origem)
    return NULL;

    no_grafo *cidade_destino=encontra_no(g,destino);
    if(!cidade_destino)
    return NULL;

    heap *fila=heap_nova(g->tamanho);
    if(!fila)
    return NULL;

    for (int i = 0; i < g->tamanho; i++)
    {
        g->nos[i]->p_acumulado=infinity;

        if (strcmp(g->nos[i]->cidade,origem)==0)
        {
           cidade_origem->p_acumulado=0;
        }

    }
    
    
    heap_insere(fila,cidade_origem,cidade_origem->p_acumulado);

    no_grafo *out;

    while (fila->tamanho > 0)
    {       
            for (int i = 0; i < fila->tamanho ; i++)
            {
                if (fila->elementos[i])
                {
                    fila->elementos[i]->prioridade=fila->elementos[i]->no->p_acumulado;
                }
            }

            out=heap_remove(fila);

            for (int i = 0; i < out->tamanho; i++)
            {
                if(difftime( mktime(&out->arestas[i]->partida) , mktime(&partida) ) > 0 )
                {   
                        if( out->arestas[i]->destino->p_acumulado > out->p_acumulado + 1)
                        {
                            out->arestas[i]->destino->p_acumulado=out->p_acumulado+1;
                            
                            out->arestas[i]->destino->anterior=out;

                            heap_insere(fila,out->arestas[i]->destino,out->arestas[i]->destino->p_acumulado);
                        }
                }
        
            }   
    }

    //criar vetor para devolver caminho 
    *n=cidade_destino->p_acumulado+1;

    no_grafo **path=calloc((*n),sizeof(no_grafo*));

    no_grafo *aux=cidade_destino;
    int tam=(*n); 
        
    while(aux!=NULL && tam > 0)   
    {
        path[tam-1]=aux;    
        aux=aux->anterior;
        tam--;
    }   
    
    heap_apaga(fila);
    
    return path;
}

aresta_grafo **atualiza_lugares(char *ficheiro, grafo *g, int *n)
{   if(!g || !ficheiro)
    return NULL;
    

    FILE *f = fopen(ficheiro, "r");
    char linha[250]={0},codigo[16]={0},lugares[4]={0},*aux;
    int pos=0,j=0,l;// l=valor de lugar extraido do ficheiro
    
    no_grafo *cidade;
    
    aresta_grafo **viagens_lotadas=(aresta_grafo **)malloc(sizeof(aresta_grafo *));
    
    while (fgets(linha,250,f)!=NULL)
    {   
        linha [strlen(linha)-1] = '\0';
        aux=strtok (linha, ",");
        strcpy(codigo,aux);
        
        codigo[strlen(codigo)]='\0';
        
        aux=strtok (NULL, ",");
        strcpy(lugares,aux);
        
        lugares[strlen(lugares)]='\0';
        l=atoi(lugares);
        
        cidade=encontra_voo(g,codigo,&pos);
        if(!cidade)
        return NULL;
            
        if (cidade->arestas[pos]->lugares!=l)
        cidade->arestas[pos]->lugares=l;
        
        if(cidade->arestas[pos]->lugares==0)
        {   
                   
                        aresta_grafo *tmp;
                        
                        tmp=cidade->arestas[pos];
                        cidade->arestas[pos]=cidade->arestas[cidade->tamanho-1];
                        cidade->arestas[cidade->tamanho-1]=tmp;
                        
                        viagens_lotadas = (aresta_grafo **)realloc(viagens_lotadas, (j + 1 ) * sizeof(aresta_grafo *));
                        j++;
                        viagens_lotadas[j-1]=tmp;               
                        
                        
                        cidade->arestas = (aresta_grafo **)realloc(cidade->arestas, (cidade->tamanho -1 ) * sizeof(aresta_grafo *));
                        cidade->tamanho--;
       
        }          
    }
    
    fclose(f);
   
    *n = j;

    return viagens_lotadas;
}


grafo *grafo_importa(const char *nome_ficheiro)
{
    if (nome_ficheiro == NULL)
        return NULL;

    FILE *f = fopen(nome_ficheiro, "r");
    if (f == NULL)
        return NULL;

    grafo *g = grafo_novo();
    if (g == NULL)
    {
        fclose(f);
        return NULL;
    }
    char str[500] = {0}, codigo[15] = {0}, origem[50] = {0}, destino[50] = {0}, companhia[4] = {0};
    int lugares = 0;
    double preco = 0;
    struct tm partida, chegada;

    char *token;
    no_grafo *no_origem, *no_destino;
    int ret;
    while (fgets(str, 500 * sizeof(char), f) != NULL)
    {
        str[strlen(str) - 1] = '\0';

        token = strtok(str, ",");
        if (!token)
            break;
        strcpy(codigo, token);

        token = strtok(NULL, ",");
        strcpy(origem, token);

        token = strtok(NULL, ",");
        strcpy(destino, token);

        token = strtok(NULL, ",");
        partida.tm_year = atoi(token);

        token = strtok(NULL, ",");
        partida.tm_mon = atoi(token) - 1;

        token = strtok(NULL, ",");
        partida.tm_mday = atoi(token);

        token = strtok(NULL, ",");
        partida.tm_hour = atoi(token);

        token = strtok(NULL, ",");
        partida.tm_min = atoi(token);

        token = strtok(NULL, ",");
        chegada.tm_year = atoi(token);

        token = strtok(NULL, ",");
        chegada.tm_mon = atoi(token) - 1;

        token = strtok(NULL, ",");
        chegada.tm_mday = atoi(token);

        token = strtok(NULL, ",");
        chegada.tm_hour = atoi(token);

        token = strtok(NULL, ",");
        chegada.tm_min = atoi(token);

        token = strtok(NULL, ",");
        preco = atof(token);

        token = strtok(NULL, ",");
        lugares = atoi(token);

        token = strtok(NULL, ",");
        strcpy(companhia, token);

        // procura no grafo um nó com o nome da origem
        no_origem = encontra_no(g, origem);
        // se o nó ainda não existe, cria-o e insere-o no grafo
        if (!no_origem)
        {

            no_origem = no_insere(g, origem);

            if (!no_origem)
            {
                fclose(f);
                return NULL;
            }
        }
        // procura no grafo um nó com o nome do destino
        no_destino = encontra_no(g, destino);

        // se o nó ainda não existe, cria-o e insere-o no grafo
        if (!no_destino)
        {
            no_destino = no_insere(g, destino);

            if (!no_destino)
            {
                fclose(f);
                return NULL;
            }
        }

        if (existe_aresta(no_origem, no_destino, codigo) == 0)
        {

            ret = cria_aresta(no_origem, no_destino, codigo, companhia, partida, chegada, preco, lugares);

            if (ret == -1)
            {
                fclose(f);
                return NULL;
            }
        }
    }

    fclose(f);
    return g;
}



//----------Funcoes auxiliares para grafo.c--------------------//

void imprime_arestas( no_grafo *no)

{
    if(!no)
    return;

    printf("\nA cidade %s apresenta %d partidas:\n",no->cidade,no->tamanho);

    for (int i = 0; i < no->tamanho; i++)
    {
        printf("Partida %d:%d do dia %d/%d/%d de %s ---> Destino ás %d:%d do dia %d/%d/%d em %s /// Codigo: %s \n",no->arestas[i]->partida.tm_hour,no->arestas[i]->partida.tm_min,no->arestas[i]->partida.tm_mday,no->arestas[i]->partida.tm_mon,no->arestas[i]->partida.tm_year,no->cidade,no->arestas[i]->chegada.tm_hour,no->arestas[i]->chegada.tm_min,no->arestas[i]->chegada.tm_mday,no->arestas[i]->chegada.tm_mon,no->arestas[i]->chegada.tm_year,no->arestas[i]->destino->cidade,no->arestas[i]->codigo);
        
    }
    printf("\n");
}



