"""
NotebookLM Client Wrapper
Wraps notebooklm-py CLI for AriseGroup automation workflows.

WARNING: Uses undocumented Google APIs that can change without notice.
Not for production client-facing systems.

Usage:
    from notebooklm_client import NotebookLMClient

    client = NotebookLMClient()
    notebook_id = client.create_notebook("PM-Discovery")
    client.upload_sources(notebook_id, ["transcript.md", "scope.pdf"])
    result = client.query(notebook_id, "Extract action items with owners")
"""

import subprocess
import json
import os
from pathlib import Path
from typing import List, Optional, Dict, Any


class NotebookLMClient:
    """Wrapper for notebooklm-py CLI."""

    def __init__(self):
        self._check_installation()

    def _check_installation(self) -> None:
        """Verify notebooklm-py is installed."""
        try:
            result = subprocess.run(
                ["notebooklm", "--version"],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                raise RuntimeError("notebooklm-py not properly installed")
        except FileNotFoundError:
            raise RuntimeError(
                "notebooklm-py not found. Install with: pip install notebooklm-py"
            )

    def is_authenticated(self) -> bool:
        """Check if Google auth is configured."""
        result = subprocess.run(
            ["notebooklm", "auth", "--check"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0

    def create_notebook(self, name: str) -> str:
        """
        Create a new notebook.

        Args:
            name: Notebook name (e.g., "PM-Discovery")

        Returns:
            Notebook ID
        """
        result = subprocess.run(
            ["notebooklm", "create", name, "--json"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(f"Failed to create notebook: {result.stderr}")

        data = json.loads(result.stdout)
        return data.get("notebook_id")

    def upload_sources(
        self,
        notebook_id: str,
        sources: List[str],
        source_type: str = "auto"
    ) -> Dict[str, Any]:
        """
        Upload source files to a notebook.

        Args:
            notebook_id: Target notebook ID
            sources: List of file paths or URLs
            source_type: "file", "url", "text", or "auto"

        Returns:
            Upload result with source IDs
        """
        results = []

        for source in sources:
            cmd = ["notebooklm", "upload", notebook_id, source]

            if source_type != "auto":
                cmd.extend(["--type", source_type])

            cmd.append("--json")

            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode != 0:
                results.append({
                    "source": source,
                    "success": False,
                    "error": result.stderr
                })
            else:
                data = json.loads(result.stdout)
                results.append({
                    "source": source,
                    "success": True,
                    "source_id": data.get("source_id")
                })

        return {
            "notebook_id": notebook_id,
            "uploads": results,
            "success_count": sum(1 for r in results if r["success"]),
            "total_count": len(results)
        }

    def query(
        self,
        notebook_id: str,
        prompt: str,
        output_format: str = "markdown"
    ) -> str:
        """
        Run a query against a notebook.

        Args:
            notebook_id: Target notebook ID
            prompt: Query prompt
            output_format: "markdown", "json", or "text"

        Returns:
            Query response
        """
        result = subprocess.run(
            [
                "notebooklm", "chat", notebook_id,
                "--prompt", prompt,
                "--format", output_format
            ],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(f"Query failed: {result.stderr}")

        return result.stdout

    def batch_query(
        self,
        notebook_id: str,
        prompts: List[str]
    ) -> List[Dict[str, str]]:
        """
        Run multiple queries against a notebook.

        Args:
            notebook_id: Target notebook ID
            prompts: List of query prompts

        Returns:
            List of query results
        """
        results = []

        for prompt in prompts:
            try:
                response = self.query(notebook_id, prompt)
                results.append({
                    "prompt": prompt,
                    "response": response,
                    "success": True
                })
            except RuntimeError as e:
                results.append({
                    "prompt": prompt,
                    "error": str(e),
                    "success": False
                })

        return results

    def generate_audio_overview(
        self,
        notebook_id: str,
        output_path: Optional[str] = None
    ) -> str:
        """
        Generate audio overview (podcast-style summary).

        Args:
            notebook_id: Target notebook ID
            output_path: Where to save the audio file

        Returns:
            Path to audio file
        """
        cmd = ["notebooklm", "audio", notebook_id]

        if output_path:
            cmd.extend(["--output", output_path])

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Audio generation failed: {result.stderr}")

        return output_path or result.stdout.strip()

    def export_notebook(
        self,
        notebook_id: str,
        output_path: str,
        format: str = "markdown"
    ) -> str:
        """
        Export notebook contents.

        Args:
            notebook_id: Target notebook ID
            output_path: Where to save export
            format: "markdown", "json", or "pdf"

        Returns:
            Path to exported file
        """
        result = subprocess.run(
            [
                "notebooklm", "export", notebook_id,
                "--output", output_path,
                "--format", format
            ],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(f"Export failed: {result.stderr}")

        return output_path


# Workflow templates for AriseGroup
QUERY_TEMPLATES = {
    "meeting_transcript": [
        "Extract all action items with clear owners and deadlines",
        "What concerns did the client raise that weren't fully addressed?",
        "Summarize key decisions made in this meeting",
        "What follow-up questions should we address in the next call?"
    ],
    "client_discovery": [
        "What are the biggest operational bottlenecks evident in these documents?",
        "What AI opportunities exist based on their current processes?",
        "What language does this client use to describe their problems?",
        "What's their current tech stack based on these sources?"
    ],
    "proposal_research": [
        "What scope elements were most valued in similar past projects?",
        "What pricing models worked best for this type of client?",
        "What objections might this client have based on our conversations?",
        "Draft an executive summary for this proposal"
    ],
    "content_repurpose": [
        "Extract 5 standalone insights that could each be a LinkedIn post",
        "What's the most contrarian take in this content?",
        "Generate 3 hook variations for the main insight",
        "What questions would a skeptic ask about this?"
    ]
}


def run_workflow(
    workflow_name: str,
    notebook_name: str,
    sources: List[str],
    output_dir: Optional[str] = None
) -> Dict[str, Any]:
    """
    Run a complete AriseGroup workflow.

    Args:
        workflow_name: One of: meeting_transcript, client_discovery,
                       proposal_research, content_repurpose
        notebook_name: Name for the notebook
        sources: List of source files to upload
        output_dir: Where to save outputs

    Returns:
        Workflow results
    """
    if workflow_name not in QUERY_TEMPLATES:
        raise ValueError(f"Unknown workflow: {workflow_name}")

    client = NotebookLMClient()

    # Create notebook
    notebook_id = client.create_notebook(notebook_name)

    # Upload sources
    upload_result = client.upload_sources(notebook_id, sources)

    # Run queries
    queries = QUERY_TEMPLATES[workflow_name]
    query_results = client.batch_query(notebook_id, queries)

    # Save outputs if directory specified
    if output_dir:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        # Save combined results
        output_file = output_path / f"{notebook_name}-output.md"
        with open(output_file, "w") as f:
            f.write(f"# {notebook_name} - NotebookLM Output\n\n")
            for result in query_results:
                if result["success"]:
                    f.write(f"## {result['prompt']}\n\n")
                    f.write(f"{result['response']}\n\n---\n\n")

    return {
        "notebook_id": notebook_id,
        "notebook_name": notebook_name,
        "workflow": workflow_name,
        "sources_uploaded": upload_result["success_count"],
        "queries_run": len(query_results),
        "results": query_results
    }


if __name__ == "__main__":
    # Test the client
    client = NotebookLMClient()
    print(f"Authenticated: {client.is_authenticated()}")
