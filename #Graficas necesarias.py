#Graficas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Supongamos que df_json es tu DataFrame
# df_json = pd.read_json('ruta/a/tu/archivo.json', lines=True)

# Configurar el estilo de seaborn
sns.set(style="whitegrid")

# Función para limitar a los 10 elementos más relevantes
def top_10(series):
    return series.value_counts().nlargest(10)

# 0. Histograma para 'spl_product_ndc'
plt.figure(figsize=(10, 5))
sns.histplot(df_json['spl_product_ndc'].value_counts(), bins=30, kde=True, color='skyblue')
plt.title('Histograma de spl_product_ndc', fontsize=14)
plt.xlabel('NDC', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.show()

# 1. Gráfico de barras para 'manufacturer_name'
plt.figure(figsize=(10, 5))
sns.countplot(y='manufacturer_name', data=df_json, order=top_10(df_json['manufacturer_name']).index, palette='viridis')
plt.title('Gráfico de barras de manufacturer_name', fontsize=14)
plt.xlabel('Cantidad', fontsize=12)
plt.ylabel('Fabricante', fontsize=12)
plt.show()

# 2. Gráfico de barras para 'application_number'
plt.figure(figsize=(10, 5))
sns.countplot(y='application_number', data=df_json, order=top_10(df_json['application_number']).index, palette='plasma')
plt.title('Gráfico de barras de application_number', fontsize=14)
plt.xlabel('Cantidad', fontsize=12)
plt.ylabel('Número de aplicación', fontsize=12)
plt.show()

# 3. Gráfico de barras apiladas para 'brand_name_suffix'
brand_suffix_counts = top_10(df_json['brand_name_suffix'])
brand_suffix_counts.plot(kind='bar', stacked=True, color='lightcoral')
plt.title('Gráfico de barras apiladas de brand_name_suffix', fontsize=14)
plt.xlabel('Sufijo de nombre de marca', fontsize=12)
plt.ylabel('Cantidad', fontsize=12)
plt.show()

# 4. Histograma para 'spl_version'
plt.figure(figsize=(10, 5))
sns.histplot(df_json['spl_version'], bins=30, kde=True, color='orange')
plt.title('Histograma de spl_version', fontsize=14)
plt.xlabel('Versión SPL', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.show()

# 5. Gráfico de barras para 'route'
plt.figure(figsize=(10, 5))
sns.countplot(y='route', data=df_json, order=top_10(df_json['route']).index, palette='magma')
plt.title('Gráfico de barras de route', fontsize=14)
plt.xlabel('Cantidad', fontsize=12)
plt.ylabel('Ruta', fontsize=12)
plt.show()

# 6. Gráfico de barras para 'generic_name'
plt.figure(figsize=(10, 5))
sns.countplot(y='generic_name', data=df_json, order=top_10(df_json['generic_name']).index, palette='cividis')
plt.title('Gráfico de barras de generic_name', fontsize=14)
plt.xlabel('Cantidad', fontsize=12)
plt.ylabel('Nombre genérico', fontsize=12)
plt.show()

# 7. Gráfico de pastel para 'brand_name'
plt.figure(figsize=(10, 5))
top_brand_names = top_10(df_json['brand_name'])
top_brand_names.plot.pie(autopct='%1.1f%%', colors=sns.color_palette("husl", len(top_brand_names)))
plt.title('Gráfico de pastel de brand_name', fontsize=14)
plt.ylabel('')
plt.show()

# 8. Gráfico de barras para 'upc'
plt.figure(figsize=(10, 5))
sns.countplot(y='upc', data=df_json, order=top_10(df_json['upc']).index, palette='Set2')
plt.title('Gráfico de barras de upc', fontsize=14)
plt.xlabel('Cantidad', fontsize=12)
plt.ylabel('UPC', fontsize=12)
plt.show()

# 9. Gráfico de barras para 'substance_name'
plt.figure(figsize=(10, 5))
sns.countplot(y='substance_name', data=df_json, order=top_10(df_json['substance_name']).index, palette='Set3')
plt.title('Gráfico de barras de substance_name', fontsize=14)
plt.xlabel('Cantidad', fontsize=12)
plt.ylabel('Nombre de sustancia', fontsize=12)
plt.show()

# 10. Gráfico de barras para ```python
# 'product_type'
plt.figure(figsize=(10, 5))
sns.countplot(y='product_type', data=df_json, order=top_10(df_json['product_type']).index, palette='Accent')
plt.title('Gráfico de barras de product_type', fontsize=14)
plt.xlabel('Cantidad', fontsize=12)
plt.ylabel('Tipo de producto', fontsize=12)
plt.show()

# 11. Histograma para 'dosage_form'
plt.figure(figsize=(10, 5))
sns.histplot(top_10(df_json['dosage_form']), bins=30, kde=True, color='lightgreen')
plt.title('Histograma de dosage_form', fontsize=14)
plt.xlabel('Forma de dosificación', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.show()

# 12. Gráfico de pastel para 'is_original_packager'
plt.figure(figsize=(10, 5))
top_is_original_packager = top_10(df_json['is_original_packager'])
top_is_original_packager.plot.pie(autopct='%1.1f%%', colors=sns.color_palette("pastel", len(top_is_original_packager)))
plt.title('Gráfico de pastel de is_original_packager', fontsize=14)
plt.ylabel('')
plt.show()

# 13. Gráfico de barras para 'rxnorm'
plt.figure(figsize=(10, 5))
sns.countplot(y='rxnorm', data=df_json, order=top_10(df_json['rxnorm']).index, palette='Dark2')
plt.title('Gráfico de barras de rxnorm', fontsize=14)
plt.xlabel('Cantidad', fontsize=12)
plt.ylabel('RxNorm', fontsize=12)
plt.show()

# 14. Histograma para 'id'
plt.figure(figsize=(10, 5))
sns.histplot(df_json['id'].value_counts(), bins=30, kde=True, color='purple')
plt.title('Histograma de id', fontsize=14)
plt.xlabel('ID', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.show()

# 15. Gráfico de pastel para 'application_number'
plt.figure(figsize=(10, 5))
top_application_number = top_10(df_json['application_number'])
top_application_number.plot.pie(autopct='%1.1f%%', colors=sns.color_palette("coolwarm", len(top_application_number)))
plt.title('Gráfico de pastel de application_number', fontsize=14)
plt.ylabel('')
plt.show()

# 16. Gráfico de barras para 'brand_name_suffix'
plt.figure(figsize=(10, 5))
sns.countplot(y='brand_name_suffix', data=df_json, order=top_10(df_json['brand_name_suffix']).index, palette='BuGn')
plt.title('Gráfico de barras de brand_name_suffix', fontsize=14)
plt.xlabel('Cantidad', fontsize=12)
plt.ylabel('Sufijo de nombre de marca', fontsize=12)
plt.show()

# 17. Gráfico de barras apiladas para 'manufacturer_name'
manufacturer_counts = top_10(df_json['manufacturer_name'])
manufacturer_counts.plot(kind='bar', stacked=True, color='salmon')
plt.title('Gráfico de barras apiladas de manufacturer_name', fontsize=14)
plt.xlabel('Fabricante', fontsize=12)
plt.ylabel('Cantidad', fontsize=12)
plt.show()

# 18. Histograma para 'route'
plt.figure(figsize=(10, 5))
sns.histplot(top_10(df_json['route']), bins=30, kde=True, color='cyan')
plt.title('Histograma de route', fontsize=14)
plt.xlabel('Ruta', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.show()

# 19. Gráfico de pastel para 'generic_name'
plt.figure(figsize=(10, 5))
top_generic_name = top_10(df_json['generic_name'])
top_generic_name.plot.pie(autopct='%1.1f%%', colors=sns.color_palette("Set1", len(top_generic_name)))
plt.title('Gráfico de pastel de generic_name', fontsize=14)
plt.ylabel('')
plt.show()