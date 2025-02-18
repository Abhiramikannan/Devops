import unittest
from process_handler import get_heavy_process, restart_application_process, terminate_process
import psutil
from unittest.mock import patch, MagicMock

class TestProcessHandler(unittest.TestCase):

    @patch('psutil.process_iter')
    def test_get_heavy_process(self, mock_process_iter):
        # Mock the process list to return processes with CPU usage > 10
        mock_proc = MagicMock()
        mock_proc.info = {'pid': 1234, 'name': 'test_process', 'cpu_percent': 15, 'username': 'user'}
        mock_process_iter.return_value = [mock_proc]

        result = get_heavy_process()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'test_process')

    @patch('psutil.Process')  # Mock psutil Process to simulate processes
    @patch('subprocess.run')  # Mock subprocess.run to prevent running real commands
    def test_restart_application_process(self, mock_subprocess, mock_psutil_process):
        # Create a mocked process
        mock_process = MagicMock()
        mock_process.info = {'pid': 5612, 'name': 'chrome.exe'}  # mock process info
        mock_psutil_process.return_value = mock_process

        # Mock subprocess.run to avoid actual system commands
        mock_subprocess.return_value = MagicMock()

        try:
            # Call the function you're testing
            restart_application_process(mock_process)
            
            # Check if terminate and wait methods were called
            mock_process.terminate.assert_called_once()
            mock_process.wait.assert_called_once()

            # Check if subprocess.run was called (simulating process restart)
            mock_subprocess.assert_called_once_with(['chrome.exe'])  # Adjust according to how it's called
        except Exception as e:
            self.fail(f"Error while testing restart: {e}")

    @patch('psutil.Process')
    def test_terminate_process(self, mock_psutil_process):
        # Mock a process to simulate termination
        mock_process = MagicMock()
        mock_process.info = {'pid': 5612, 'name': 'chrome.exe'}
        mock_psutil_process.return_value = mock_process

        try:
            terminate_process(mock_process)
            mock_process.terminate.assert_called_once()
            mock_process.wait.assert_called_once()
        except Exception as e:
            self.fail(f"Error while testing termination: {e}")

if __name__ == '__main__':
    unittest.main()
