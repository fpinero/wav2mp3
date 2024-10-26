#!/usr/bin/env python3
"""
Script para convertir archivos WAV a MP3.
"""

from pathlib import Path
from pydub import AudioSegment
import sys
import logging

# Configuración del logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AudioConverter:
    """Clase para manejar la conversión de archivos WAV a MP3."""
    
    @staticmethod
    def convert_wav_to_mp3(input_path: Path) -> bool:
        """
        Convierte un archivo WAV a MP3.
        
        Args:
            input_path (Path): Ruta del archivo WAV a convertir
            
        Returns:
            bool: True si la conversión fue exitosa, False en caso contrario
        """
        try:
            # Verificar que el archivo existe y es WAV
            if not input_path.exists():
                logger.error(f"El archivo {input_path} no existe")
                return False
            
            if input_path.suffix.lower() != '.wav':
                logger.error(f"El archivo {input_path} no es un archivo WAV")
                return False
            
            # Crear la ruta de salida para el MP3
            output_path = input_path.with_suffix('.mp3')
            
            logger.info(f"Convirtiendo {input_path.name} a MP3...")
            
            # Usar str(input_path) y str(output_path) para manejar correctamente los espacios
            audio = AudioSegment.from_wav(str(input_path))
            audio.export(str(output_path), format='mp3')
            
            logger.info(f"Conversión completada: {output_path.name}")
            return True
            
        except Exception as e:
            logger.error(f"Error durante la conversión: {str(e)}")
            return False

def main():
    """Función principal del script."""
    try:
        # Solicitar la ruta del archivo y limpiar la entrada
        input_path_str = input("Introduce la ruta del archivo WAV a convertir: ").strip()
        
        # Eliminar comillas si el usuario las incluyó
        input_path_str = input_path_str.strip('"').strip("'")
        
        # Convertir a Path (pathlib maneja automáticamente los espacios)
        input_path = Path(input_path_str).resolve()
        
        converter = AudioConverter()
        success = converter.convert_wav_to_mp3(input_path)
        
        if not success:
            sys.exit(1)
            
    except KeyboardInterrupt:
        logger.info("\nProceso interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
