"""
Hybrid Hacking Toolkit - Main Entry Point
A desktop cyber toolkit with Kali Linux inspired interface
"""

import sys
import argparse
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import Qt, QTimer
from core.identity_checker import IdentityChecker, IdentityError
from ui.main_window import MainWindow
from ui.styles import COLORS


def show_error_dialog(error_message: str):
    """
    Display a cyber-styled error dialog
    
    Args:
        error_message: The error message to display
    """
    app = QApplication(sys.argv)
    app.setStyleSheet(f"""
        QMessageBox {{
            background-color: {COLORS['bg_primary']};
            color: {COLORS['text_primary']};
        }}
        QMessageBox QLabel {{
            color: {COLORS['text_primary']};
            background-color: {COLORS['bg_primary']};
            padding: 10px;
        }}
        QMessageBox QPushButton {{
            background-color: {COLORS['bg_tertiary']};
            color: {COLORS['accent']};
            border: 1px solid {COLORS['accent']};
            border-radius: 5px;
            padding: 8px 20px;
            font-weight: bold;
            min-width: 80px;
        }}
        QMessageBox QPushButton:hover {{
            background-color: {COLORS['accent']};
            color: {COLORS['bg_primary']};
        }}
    """)
    
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.setWindowTitle("Identity Verification Failed")
    msg.setText("IDENTITY VERIFICATION ERROR")
    msg.setInformativeText(error_message)
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.exec()
    
    sys.exit(1)


def verify_identity(identity_path: str = None, consent_path: str = None, dry_run: bool = False) -> bool:
    """
    Verify identity and consent files
    
    Args:
        identity_path: Custom path to identity.txt
        consent_path: Custom path to consent.txt
        dry_run: If True, only verify and print summary, don't launch GUI
        
    Returns:
        True if verification succeeds
        
    Raises:
        IdentityError: If verification fails
    """
    try:
        checker = IdentityChecker(identity_path=identity_path, consent_path=consent_path)
        checker.verify_all()
        
        # Print summary
        checker.print_summary()
        
        if dry_run:
            print("Dry-run mode: Verification successful. Exiting.")
            return True
        
        return True
        
    except IdentityError as e:
        if dry_run:
            print(f"\n[ERROR] Identity verification failed:\n{str(e)}\n")
            return False
        else:
            show_error_dialog(str(e))
            return False
    except Exception as e:
        error_msg = f"Unexpected error during verification:\n{str(e)}"
        if dry_run:
            print(f"\n[ERROR] {error_msg}\n")
            return False
        else:
            show_error_dialog(error_msg)
            return False


def main():
    """Initialize and run the application"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Hybrid Hacking Toolkit - Desktop cyber toolkit with Kali Linux inspired interface",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Verify identity files only, do not launch GUI'
    )
    parser.add_argument(
        '--identity',
        type=str,
        default=None,
        help='Custom path to identity.txt file'
    )
    parser.add_argument(
        '--consent',
        type=str,
        default=None,
        help='Custom path to consent.txt file'
    )
    
    args = parser.parse_args()
    
    # Verify identity before launching GUI
    if not verify_identity(
        identity_path=args.identity,
        consent_path=args.consent,
        dry_run=args.dry_run
    ):
        if args.dry_run:
            sys.exit(1)
        # If not dry-run, show_error_dialog already exits
        return
    
    # If dry-run, exit here
    if args.dry_run:
        sys.exit(0)
    
    # Initialize and run the application
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Kali Linux For Your Windows")
    app.setOrganizationName("KaliToolkit")
    
    # Show splash screen
    from ui.splash_screen import CyberSplashScreen
    splash = CyberSplashScreen()
    splash.show()
    splash.show_message("Initializing toolkit...")
    app.processEvents()
    
    # Create main window
    window = MainWindow()
    
    # Update splash
    splash.show_message("Loading modules...")
    app.processEvents()
    
    # Simulate loading time
    QTimer.singleShot(1500, lambda: None)
    app.processEvents()
    
    # Show main window and close splash
    window.show()
    splash.finish(window)
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

