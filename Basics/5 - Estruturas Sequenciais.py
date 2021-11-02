#!/usr/bin/env python
# coding: utf-8

# In[19]:


idade = input("Informe a sua idade: ")
print(idade, type(idade))


# In[24]:


idade = int(idade)
print(idade, type(idade))


# In[26]:


print(float('123.52'))
print(str(123.25))
print(bool(''))
print(bool('abc'))
print(bool(0))
print(bool(-2))


# In[32]:


salario = input("Qual o seu salário?")
salario = float(salario)

gasto = input("Gastos totais")
gasto = float(gasto)

salario_total = salario * 12
gasto_total = gasto * 12

montante = salario_total - gasto_total
print("O montante economizado é", montante)


# In[ ]:




